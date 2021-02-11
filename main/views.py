from django.db.models import Sum

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin

from .serializers import CourseSerializer, CoursePriceSerializer, CourseWithSectionSerializer, SectionSerializer
from .models import Course, Section


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(methods=['GET'], detail=True, serializer_class=CoursePriceSerializer)
    def price(self, request, pk):

        object = get_object_or_404(Course.objects.annotate(course_price=Sum('sections__price')), pk=pk)
        return Response(self.get_serializer(object).data)


class SectionViewSet(ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class CourseWithSectionsViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    queryset = Course.objects.all().prefetch_related('sections')
    serializer_class = CourseWithSectionSerializer


