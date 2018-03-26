from django.core.mail.backends import console
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser
from rest_framework import status, viewsets
from rest_framework.views import APIView
from .models import UserProfile, Companies
from django.contrib.auth.models import User
from .serializers import (UserSerializer, 
                          CreateUserSerializer, 
                          DisplayUserProfileSerializer, 
                          CompanySerializer,
                          Screen1Serializer,
                          Screen2Serializer,
                          Screen3Serializer,
                          Screen4Serializer,
                          Screen5Serializer, 
                          DisplayCompanySerializer)
from django.core import serializers
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
import logging
from django.utils.six import BytesIO


logger = logging.getLogger()


class UserViewSet(viewsets.ModelViewSet):
    authentication_class = (JSONWebTokenAuthentication,)  # Don't forget to add a 'comma' after first element to make it a tuple
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save()


@api_view(['POST'])
@permission_classes((AllowAny,))
def create_user(request):
    print("hello1")
    serialized = UserSerializer(data=request.data)
    print(serializers)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyViewSet(viewsets.ModelViewSet):
    authentication_class = (JSONWebTokenAuthentication,)
    queryset = Companies.objects.all()
    # print("this is queryset ")
    print(queryset)
    serializer_class = CompanySerializer
    print(serializer_class)
    permission_classes = (IsAuthenticated, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save()


@api_view(['POST'])
@permission_classes((AllowAny,))
def create_company(request):
    serialized = CompanySerializer(data=request.data)
    # print(serializers)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})


class UserRegistration(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        snippets = UserProfile.objects.all()
        print(snippets)
        serializer = CreateUserSerializer(snippets, many=True)
        # print(serializer)
        return Response(serializer.data)

    def post(self, request):
        print(request.POST['user'])
        user = UserProfile.objects.filter(pk=request.POST['user']).update(
            country=request.POST['country'],
            full_name=request.POST['full_name'],
            age=request.POST['age'],
            date_of_birth=request.POST['date_of_birth'],
            address=request.POST['address'],
            phone=request.POST['phone'],
            email=request.POST['email'],
        )
        print(user)
        print(request.POST['country'])
        serializer = CreateUserSerializer(data=request.POST)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request):
    #     user = request.user
    #     logging.debug(user)
    #     serializer = CreateUserSerializer(data=request.POST)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        # UserProfile.objects.create(
        #     user=user,
        #     country='Cambodia',
        #     full_name='bobo',
        # )

class SubmitScreen2View(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        print(request.POST['user'])
        user = UserProfile.objects.filter(pk=request.POST['user']).update(
            job=request.POST['job'],
            location=request.POST['location'],
            expect_salary=request.POST['expect_salary'],
            payment_method=request.POST['payment_method'],
            salary_duration=request.POST['salary_duration'],
        )
        print(user)
        serializer = CreateUserSerializer(data=request.POST)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

class SubmitScreen3View(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        print(request.POST['user'])
        user = UserProfile.objects.filter(pk=request.POST['user']).update(
            current_designation=request.POST['current_designation'],
            working_years_cc=request.POST['working_years_cc'],
            skills=request.POST['skills'],
            experiences=request.POST['experiences'],
            no_coworker=request.POST['no_coworker'],
            disability=request.POST['disability'],
            department=request.POST['department'],
            current_salary=request.POST['current_salary'],
            current_salary_duration=request.POST['current_salary_duration'],
        )
        print(user)
        serializer = CreateUserSerializer(data=request.POST)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class SubmitScreen4View(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        print(request.POST['user'])
        user = UserProfile.objects.filter(pk=request.POST['user']).update(
            family_member=request.POST['family_member'],
            father_occupation=request.POST['father_occupation'],
            no_siblings=request.POST['no_siblings'],
            no_relative=request.POST['no_relative'],
            current_asset=request.POST['current_asset'],
        )
        print(user)
        serializer = CreateUserSerializer(data=request.POST)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class SubmitScreen5View(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        print(request.POST['user'])
        user = UserProfile.objects.filter(pk=request.POST['user']).update(
            training=request.POST['training'],
            duration_training=request.POST['duration_training'],
        )
        print(user)
        serializer = CreateUserSerializer(data=request.POST)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class DisplayUserProfileView(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user_id = []
        email_ = []
        jsonformat = mdict()
        user_profile = UserProfile.objects.all()
        for i in user_profile:
            user = User.objects.get(pk=i.id)
            print(i.user.username)
            email_.append(i.user.email)
            user_id.append(i.user.id)
        users = UserProfile.objects.all()
        serializer1 = Screen1Serializer(users, many=True)
        serializer2 = Screen2Serializer(users, many=True)
        serializer3 = Screen3Serializer(users, many=True)
        serializer4 = Screen4Serializer(users, many=True)
        serializer5 = Screen5Serializer(users, many=True)
        for i in range(len(email_)):
            jsonformat['msg'] = {user_id[i]: { 
                                 's1': serializer1.data[i],
                                 's2': serializer2.data[i],
                                 's3': serializer3.data[i],
                                 's4': serializer4.data[i],
                                 's5': serializer5.data[i],}
                                 }
        return Response(jsonformat)

        
class DisplayUserProfileForWebView(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user_name = []
        user_email = []
        jsonformat = mdict()
        user_profile = UserProfile.objects.all()
        for i in user_profile:
            print(i.user.username)
            user_name.append(i.user.username)  #get value form queryset object from User
            user_email.append(i.user.email)
        users = UserProfile.objects.all()
        serializer = DisplayUserProfileSerializer(users, many=True)
        for i in range(len(user_name)):
            jsonformat['msg'] = {'userprofile': serializer.data[i],
                                 'username': user_name[i],
                                 'email': user_email[i],
                                 }
        return Response(jsonformat)


class DisplayCompanyView(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        company_name = []
        compnay_email = []
        jsonformat = mdict()
        company = Companies.objects.filter(company_name_type=2)
        print(company)
        for i in company:
            # user = User.objects.get(pk=i.id)
            print(i.company_user.username)
            company_name.append(i.company_user.username)
            compnay_email.append(i.company_user.email)
        for i in range(len(company_name)):
            jsonformat['msg'] = {'companyname': company_name[i],
                                 'companyemail': compnay_email[i],
                                 }
        return Response(jsonformat)


class DisplayAllUsersView(APIView):
    def get(self, request):
        companies = User.objects.all()
        serializer = UserSerializer(companies, many=True)
        print(serializer)
        return Response(serializer.data)


class mdict(dict):

    def __setitem__(self, key, value):
        """add the given value to the list of values for this key"""
        self.setdefault(key, []).append(value)