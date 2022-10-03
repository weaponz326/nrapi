import datetime
import json
from secrets import compare_digest

from django.conf import settings
from django.db.transaction import atomic, non_atomic_requests
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils import timezone

# from suites.restaurant.modules.settings.models import Subscription, SubscriptionEvent


# Create your views here.

@csrf_exempt
@require_POST
@non_atomic_requests
def payments_webhook(request):
    payload = json.loads(request.body)
    # process_webhook_payload(payload)
    return HttpResponse()

# @atomic
# def process_webhook_payload(payload):
#     customer_code = payload['customer']['cusotmer_code']

#     event = ''
#     amount = payload['plan']['amount'] / 100

#     subscription = Subscription.objects.filter(customer_code=customer_code)

#     if payload['event'] == 'subscription.create':
#         event = 'Subscription created'
#         subscription.objects.update(status='Pending')

#     elif payload['event'] == 'subscription.disable':
#         event = 'Subscription Cancelled'
#         subscription.objects.update(status='Cancelled')

#     elif payload['event'] == 'charge.success':
#         event = 'Transaction successful'
#         subscription.objects.update(status='Active')

#     account = subscription['account']

#     SubscriptionEvent.objects.create(
#         account = account,
#         event = event,
#         amount = amount,
#     )