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
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = TablePagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name']

class UserDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
