import datetime
from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncDate

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import api_view

from .models import Note
from .serializers import NoteSerializer
from users.paginations import TablePagination
from users.services import fillZeroDates


# Create your views here.

class NoteView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['title', 'created_at', 'updated_at']
    ordering = ['-created_at']

    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        note = Note.objects.filter(user=user)
        results = self.paginate_queryset(note, request, view=self)
        serializer = NoteSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NoteDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        note = Note.objects.get(id=id)
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        note = Note.objects.get(id=id)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        note = Note.objects.get(id=id)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class NoteSearchView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'body']

# --------------------------------------------------------------------------------------
# dashboard

@api_view()
def note_count(request):
    count = Note.objects\
        .filter(user__id=request.query_params.get('user', None))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .count()           
    content = {'count': count}
    return Response(content)

@api_view()
def note_annotate(request):
    items = Note.objects\
        .filter(user__id=request.query_params.get('user', None))\
        .annotate(date=TruncDate('created_at'))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .values('date').annotate(count=Count('id')).order_by('-date')
    filled_items = fillZeroDates(items)
    return Response(filled_items)

