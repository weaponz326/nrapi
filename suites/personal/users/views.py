from django.shortcuts import render

from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer
from .paginations import TablePagination


# Create your views here.

# user search

class UserSearchView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name']
    pagination_class = TablePagination

    def get_queryset(self):
        query_params = self.request.query_params
        user = query_params.get('user', None)
        queryset = User.objects.all().exclude(id=user)
        return queryset

class UserDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
