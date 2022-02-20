from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import generics, status, mixins
from rest_framework.response import Response

# Create your views here.


class StudentView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin,mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'

    def post(self, request):
        return self.create(request)

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)
