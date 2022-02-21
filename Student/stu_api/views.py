from .models import Student
from .serializers import StudentSerializer
from rest_framework import generics
from .validation import RollValidation
# Create your views here.


class StudentListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        self.clean()
        return self.create(request)

    def get(self, request, *args, **kwargs):
        return self.list(request)


class StudentUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request)

    def put(self, request, *args, **kwargs):
        return self.update(request)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request)
