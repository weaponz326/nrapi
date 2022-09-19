import datetime
from django.shortcuts import render
from django.db.models.functions import TruncDate
from django.db.models import Count

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins, status, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

from .models import Rink
from .serializers import RinkNestedSerializer, RinkSerializer
from users.services import fillZeroDates


# Create your views here.

class RinkView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        rink = Rink.objects.filter(user=user)
        serializer = RinkSerializer(rink, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RinkSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class RinkDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        rink = Rink.objects.get(id=id)
        serializer = RinkNestedSerializer(rink)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        rink = Rink.objects.get(id=id)
        serializer = RinkSerializer(rink, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        rink = Rink.objects.get(id=id)
        rink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# list all incoming and outgoing rinks of a user
class AllRinkView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RinkNestedSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at']
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = Rink.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(sender__id=user) | queryset.filter(recipient__id=user)
        return queryset

# --------------------------------------------------------------------------------------
# dashboard

@api_view()
def rink_share_count(request):
    rink_in = Rink.objects\
        .filter(recipient__id=request.query_params.get('user', None))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .count()
    
    rink_out = Rink.objects\
        .filter(sender__id=request.query_params.get('user', None))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .count()
                    
    content = {'rink_in': rink_in, 'rink_out': rink_out}
    return Response(content)

@api_view()
def rink_share_annotate(request):
    rink_in_items = Rink.objects\
        .filter(recipient__id=request.query_params.get('user', None))\
        .annotate(date=TruncDate('created_at'))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .values('date').annotate(count=Count('id')).order_by('-date')
    filled_rink_in_items = fillZeroDates(rink_in_items)

    rink_out_items = Rink.objects\
        .filter(sender__id=request.query_params.get('user', None))\
        .annotate(date=TruncDate('created_at'))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .values('date').annotate(count=Count('id')).order_by('-date')
    filled_rink_out_items = fillZeroDates(rink_out_items)

    content = {'rink_in': filled_rink_in_items, 'rink_out': filled_rink_out_items}
    return Response(content)
