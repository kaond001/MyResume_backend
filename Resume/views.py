from django.shortcuts import render
# Create your views here.
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Contact, Education, Home, Media,Skills, Testimonials
from .serializers import ContactSerializer, EducationSerializer, HomeSerializer, MediaSerializer,SkillsSerializer, TestimonialsSerializer
from rest_framework.decorators import api_view
# class HelloView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def get(self, request):
#         content = {'message': 'Hello, World!'}
#         return Response(content)

@api_view(['GET', 'POST'])
def Contact_list(request):
    if request.method == 'GET':
        contact = Contact.objects.all()
        Contact_serializer = ContactSerializer(contact, many=True)
        return JsonResponse(Contact_serializer.data, safe=False)

    elif request.method == 'POST':
        contact_data = JSONParser().parse(request)
        contact_serializer = ContactSerializer(data=contact_data)
        if contact_serializer.is_valid():
            contact_serializer.save()
            return JsonResponse(contact_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(contact_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def Skills_list(request):
    if request.method == 'GET':
        skill = Skills.objects.all()
        Skills_serializer = SkillsSerializer(skill, many=True)
        return JsonResponse(Skills_serializer.data, safe=False)

    elif request.method == 'POST':
        skills_data = JSONParser().parse(request)
        skills_serializer = SkillsSerializer(data=skills_data)
        if skills_serializer.is_valid():
            skills_serializer.save()
            return JsonResponse(skills_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(skills_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def Education_list(request):
    if request.method == 'GET':
        education = Education.objects.all()
        Education_serializer = EducationSerializer(education, many=True)
        return JsonResponse(Education_serializer.data, safe=False)

    elif request.method == 'POST':
        education_data = JSONParser().parse(request)
        education_serializer = EducationSerializer(data=education_data)
        if education_serializer.is_valid():
            education_serializer.save()
            return JsonResponse(education_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(education_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def Home_list(request):
    if request.method == 'GET':
        home = Home.objects.all()
        Home_serializer = HomeSerializer(home, many=True)
        return JsonResponse(Home_serializer.data, safe=False)

    elif request.method == 'POST':
        home_data = JSONParser().parse(request)
        home_serializer = HomeSerializer(data=home_data)
        if home_serializer.is_valid():
            home_serializer.save()
            return JsonResponse(home_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(home_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def Testimonial_list(request):
    if request.method == 'GET':
        testmonial = Testimonials.objects.all()
        testmonial_serializer = TestimonialsSerializer(testmonial, many=True)
        return JsonResponse(testmonial_serializer.data, safe=False)

    elif request.method == 'POST':
        testmonial_data = JSONParser().parse(request)
        testmonial_serializer = TestimonialsSerializer(data=testmonial_data)
        if testmonial_serializer.is_valid():
            testmonial_serializer.save()
            return JsonResponse(testmonial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(testmonial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def Testimonial_list(request):
    if request.method == 'GET':
        testmonial = Testimonials.objects.all()
        testmonial_serializer = TestimonialsSerializer(testmonial, many=True)
        return JsonResponse(testmonial_serializer.data, safe=False)

    elif request.method == 'POST':
        testmonial_data = JSONParser().parse(request)
        testmonial_serializer = TestimonialsSerializer(data=testmonial_data)
        if testmonial_serializer.is_valid():
            testmonial_serializer.save()
            return JsonResponse(testmonial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(testmonial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def Media_list(request):
    if request.method == 'GET':
        media = Media.objects.all()
        media_serializer = MediaSerializer(media, many=True)
        return JsonResponse(media_serializer.data, safe=False)

    elif request.method == 'POST':
        media_data = JSONParser().parse(request)
        media_serializer = MediaSerializer(data=media_data)
        if media_serializer.is_valid():
            media_serializer.save()
            return JsonResponse(media_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(media_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


