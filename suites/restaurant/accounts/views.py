from functools import partial
from django.shortcuts import render
from django.contrib.sessions.backends.db import SessionStore

from rest_framework.response import Response
from rest_framework import generics, request, status
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.views import APIView

from .models import Account
from .serializers import AccountSerializer
from suites.personal.users.paginations import TablePagination


# Create your views here.

class AccountView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        account = Account.objects.filter(account=account)
        serializer = AccountSerializer(account, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AccountSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class AccountDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        account = Account.objects.get(id=id)
        serializer = AccountSerializer(account)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        account = Account.objects.get(id=id)
        serializer = AccountSerializer(account, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        account = Account.objects.get(id=id)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------------------------

# restaurant search
        
class AccountSearchView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AccountSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    pagination_class = TablePagination

    def get_queryset(self):
        query_params = self.request.query_params
        account = query_params.get('account', None)
        queryset = Account.objects.all().exclude(id=account)
        return queryset
