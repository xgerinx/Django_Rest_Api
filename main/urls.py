from django.urls import path, include
from rest_framework import routers

from .views import CourseViewSet, CourseWithSectionsViewSet, SectionViewSet

router = routers.SimpleRouter()
router.register('courses/with-sections', CourseWithSectionsViewSet, basename='courses-with-sections')
router.register('courses', CourseViewSet, basename='courses')
router.register('sections', SectionViewSet, basename='sections')

urlpatterns = [
    path('', include(router.urls)),
]
