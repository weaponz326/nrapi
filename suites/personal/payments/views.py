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
from suites.restaurant.accounts.models import Account


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

    # subscription charged
    if payload['event'] == 'charge.success':
        subscription = Subscription.objects.get(email=email, status='Pending')
        subscription.customer_code = customer_code
        subscription.status = 'Active'
        subscription.save()

        SubscriptionEvent.objects.create(
            account = Account.objects.get(id=subscription.id),
            event = 'Subscription Charge Successful',
            amount = amount,
        )

    # subscription created
    elif payload['event'] == 'subscription.create':
        subscription = Subscription.objects.filter(email=email, customer_code=customer_code)
        subscription.subscription_code = payload['data']['subscription_code']
        subscription.status = 'Cancelled'

        SubscriptionEvent.objects.create(
            account = Account.objects.get(id=subscription.id),
            event = 'Subscription Created',
            amount = amount,
        )
        
    # subscription cancelled
    elif payload['event'] == 'subscription.not_renew':
        subscription = Subscription.objects.filter(email=email, customer_code=customer_code)
        subscription.status = 'Cancelled'
        subscription.save()

        SubscriptionEvent.objects.create(
            account = Account.objects.get(id=subscription.id),
            event = 'Subscription Cancelled',
            amount = amount,
        )

