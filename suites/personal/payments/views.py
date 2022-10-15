import datetime
import json
from secrets import compare_digest

from django.conf import settings
from django.db.transaction import atomic, non_atomic_requests
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils import timezone

from suites.restaurant.modules.settings.models import Subscription, SubscriptionEvent


# Create your views here.

@csrf_exempt
@require_POST
@non_atomic_requests
def payments_webhook(request):
    payload = json.loads(request.body)
    process_webhook_payload(payload)
    return HttpResponse()

@atomic
def process_webhook_payload(payload):
    print(payload)

    email = payload['data']['customer']['email']
    customer_code = payload['data']['customer']['customer_code']
    amount = payload['data']['amount'] / 100

    # subscription created
    if payload['event'] == 'subscription.create':
        subscription = Subscription.objects.filter(email=email, status='Pending')

        subscription.update(
            customer_code = customer_code,
            subscription_code = payload['data']['subscription_code']
        )

        SubscriptionEvent.objects.create(
            account = subscription.account,
            event = 'Subscription Created',
            amount = amount,
        )
        
    # subscription cancelled
    elif payload['event'] == 'subscription.disable':
        subscription = Subscription.objects.filter(customer_code=customer_code)
        subscription.update(status='Cancelled')

        SubscriptionEvent.objects.create(
            account = subscription.account,
            event = 'Subscription Cancelled',
            amount = amount,
        )

    # subscription charged
    elif payload['event'] == 'charge.success':
        subscription = Subscription.objects.filter(customer_code=customer_code)
        subscription.update(status='Active')

        SubscriptionEvent.objects.create(
            account = subscription.account,
            event = 'Subscription Successful',
            amount = amount,
        )
