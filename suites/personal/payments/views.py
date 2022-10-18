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
            event = 'Payment Successful',
            amount = amount,
        )

    # subscription created
    elif payload['event'] == 'subscription.create':
        SubscriptionEvent.objects.create(
            account = Account.objects.get(id=subscription.id),
            event = 'Subscription Created',
            amount = amount,
        )
        
    # subscription cancelled
    elif payload['event'] == 'subscription.not_renew':
        SubscriptionEvent.objects.create(
            account = Account.objects.get(id=subscription.id),
            event = 'Subscription Cancelled',
            amount = amount,
        )

    # subscription disabled
    elif payload['event'] == 'subscription.disable':
        subscription = Subscription.objects.get(email=email, customer_code=customer_code)
        subscription.status = 'Disabled'
        subscription.save()

        SubscriptionEvent.objects.create(
            account = Account.objects.get(id=subscription.id),
            event = 'Subscription Cancelled',
            amount = amount,
        )

    # subscription cancelled
    elif payload['event'] == 'invoice.payment_failed':
        SubscriptionEvent.objects.create(
            account = Account.objects.get(id=subscription.id),
            event = 'Payment',
            amount = amount,
        )