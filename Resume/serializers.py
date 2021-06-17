from rest_framework.serializers import ModelSerializer
from .models import Contact, Education, Home, Media,Skills, Testimonials


class ContactSerializer(ModelSerializer):

    class Meta:
        model = Contact

        fields = ['id', 'full_name', 'area', 'city', 'email', 'country', 'phone', 'created_on', 'status']


class SkillsSerializer(ModelSerializer):

    class Meta:
        model = Skills

        fields = ['id', 'skill_name','percentage', 'color_code', 'created_on']

class EducationSerializer(ModelSerializer):

    class Meta:
        model = Education

        fields = ['id', 'institute_name','programm', 'Year_of_graduate', 'created_on']


class HomeSerializer(ModelSerializer):

    class Meta:
        model = Home

        fields = ['id', 'heading','summary', 'created_on']

class TestimonialsSerializer(ModelSerializer):

    class Meta:
        model = Testimonials

        fields = ['id', 'message','user', 'created_on']

class MediaSerializer(ModelSerializer):

    class Meta:
        model = Media

        fields = ['id', 'icon','name', 'created_on']