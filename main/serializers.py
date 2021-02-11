from rest_framework import serializers

from .models import Course, Section


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CoursePriceSerializer(serializers.ModelSerializer):
    course_price = serializers.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        model = Course
        fields = ('name', 'course_price')


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class SectionWithoutPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        exclude = ('id', 'course')
        extra_kwargs = {
            'price': {'write_only': True},
        }


class CourseWithSectionSerializer(serializers.ModelSerializer):
    sections = SectionWithoutPriceSerializer(many=True)

    class Meta:
        model = Course
        fields = ('name', 'sections')

    def create(self, validated_data):
        sections_data = validated_data.pop('sections')
        course = Course.objects.create(**validated_data)

        objs = []
        for i in sections_data:
            objs.append(Section(course=course, **i))

        Section.objects.bulk_create(objs)
        return course
