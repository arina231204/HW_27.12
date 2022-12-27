from django.shortcuts import render
from rest_framework import viewsets, generics

from study.models import Courses, Student, Mentor

from .serializers import CoursesSerializer, StudentSerializer, MentorSerializer

from .my_generics import *


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer


class StudentCreateListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class MentorListCreateAPIView(ListMixinAPI, CreateMixinAPI, MYAPIView):
    serializer_class = MentorSerializer
    model = Mentor

    def get(self, request, *args, **kwargs):
        return self.list(request, *args,**kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs )

class MentorRetrieveUpdateDestroyAPIView(UpdateMixinAPI, RetrieveMixinAPI, DeleteMixinAPI, MYAPIView):
    serializer_class = MentorSerializer
    model = Mentor

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# class MentorFrankensteinViewSet(ListMixinAPI,CreateMixinAPI,UpdateMixinAPI,RetrieveMixinAPI,DeleteMixinAPI,MYAPIView):
#     serializer_class = MentorSerializer
#     model = Mentor
#     queryset = Mentor.objects.all()