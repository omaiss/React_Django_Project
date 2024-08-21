from django.shortcuts import render
from .serializers import UserViewSerializer, CustomUserAddSerializer
from rest_framework.serializers import Serializer
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Custom_User
from rest_framework.views import APIView
from .emails import send_otp
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserViewSerializer
    
class UserAdd(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserViewSerializer(data = data)
            if serializer.is_valid():
                if User.objects.filter(email = serializer.validated_data['email']): # type: ignore
                    return Response({
                        'status':400,
                        'message': 'User already exists!',
                        'data':serializer.errors
                    })                
                serializer.save()
                send_otp(serializer.data['email']) # type: ignore
                return Response({
                    'status':200,
                    'message':'Registration success!',
                    'data': serializer.data
                })            
        except Exception as E:
            print(E)
            return Response({
                'status':400,
                'message': 'Something went wrong!',
                'data':serializer.errors
            })


class VerifyOTP(APIView):
    def post(self, request):
        try:
            print(request.data)
            email = request.data['email']
            otp = ''.join(request.data['otp'])
            user = User.objects.filter(email = email)
            if not user:
                return Response({
                    'status':400,
                    'message': "User doesn't exist",
                }, status=status.HTTP_400_BAD_REQUEST)
            print(user[0].otp, otp)
            if not user[0].otp == otp:
                return Response({
                    'status':400,
                    'message': "Wrong Otp",
                    'data': 'Wrong Otp'
                }, status=status.HTTP_400_BAD_REQUEST)
                
            return Response({
                'status' : 200,
                'message' : 'User verified!' 
            }, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            
class Resend_OTP(APIView):
    def post(self, request):
        try:
            data = request.data
            send_otp(data['email'])                
            return Response({
                'status':200,
                'message':'OTP resent successfully!',            
            })            
        except Exception as E:
            print(E)
            return Response({
                'status':400,
                'message': 'Something went wrong!',
            })


class UserLogin(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email, password=password).values()
        if user.exists():
            return JsonResponse({'status': 200, 'message': 'Login successful'}, status=200)
        else:
            return JsonResponse({'status': 400, 'message': 'Invalid credentials'}, status=400)    
        
        
class CustomUserAdd(APIView):
    def post(self, request):
        try:
            data = request.data
            email = data['email']
            if Custom_User.objects.filter(email=email):
                return Response({
                'status':400,
                'message': 'Custom User already exists!',
                }, status=400)
            print(data)
            serializer = CustomUserAddSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                print(f'User added with crenditials: {serializer.data}')
                return Response({
                    'status': 200,
                    'message': 'Custom User added successfully!',
                }, status=200)
        except Exception as e:
                return Response({
                'status':400,
                'message': 'Invalid Credentials',
                }, status=400)
            
        

        