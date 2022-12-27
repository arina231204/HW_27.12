from rest_framework import viewsets, serializers

from study.models import Courses, Student, Mentor


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class MentorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=225)
    experience = serializers.IntegerField()


    def save(self,**kwargs):
        print('creating new message')
        return super().save(**kwargs)


    def create(self, validated_data):
        mentor = Mentor.objects.create(
            name = validated_data['name'],
            experience = validated_data['experience'],
        )
        return mentor

    def update(self, instance,validated_data):
        instance.name = validated_data['name']
        instance.experience = validated_data['experience']
        instance.save()
        return instance