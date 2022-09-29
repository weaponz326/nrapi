import datetime
import json
from secrets import compare_digest


from django.conf import settings
from django.db.transaction import atomic, non_atomic_requests
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils import timezone

# from example.core.models import CodeunderscoredWebhookMessage


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
    # TODO: business logic
    pass