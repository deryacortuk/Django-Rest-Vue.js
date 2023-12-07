from django.shortcuts import render
from .serializers import RegisterSerializer,LoginSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework import viewsets, status, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from account.models import User
from rest_framework_simplejwt import authentication

def index(request):
    return render(request,"index.html")


class RegisterViewSet(ViewSet):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']     
     
   
    def create(self, request, *args, **kwargs):  
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = {
        "refresh": str(refresh),
         "access": str(refresh.access_token),
         }
      
        return Response({ "user": serializer.data, "refresh": res["refresh"], "token": res["access"] }, status=status.HTTP_201_CREATED)
                 
       

class LoginViewSet(ViewSet):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post'] 
     
    
    def create(self, request, *args, **kwargs):
        serializer =  self.serializer_class(data=request.data)
        try:            
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


    
        
    
class RefreshViewSet(ViewSet, TokenRefreshView):
    
    permission_classes = (AllowAny,)
    http_method_names = ['post']
    
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        return Response(serializer.validated_data,   status=status.HTTP_200_OK)      
        

class LogoutViewSet(ViewSet):
    authentication_classes = ()
    permission_classes = (permissions.IsAuthenticated,)
    http_method_names = ["post"]
    
    
    def create(self, request, *args, **kwargs):
        
        refresh = request.data.get("refresh")
        if refresh is None:
            raise ValidationError({"detail": "A refresh token is required."})
        try:
            token = RefreshToken(request.data.get("refresh"))
            token.blacklist()
            return Response( status=status.HTTP_204_NO_CONTENT)
        except TokenError:
            raise ValidationError({"detail":"The refresh token is invalid."})
        
class DecoratedTokenObtainPairView(ViewSet,TokenObtainPairView):
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
class DecoratedTokenRefreshView(ViewSet,TokenRefreshView):
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
class DecoratedTokenVerifyView(ViewSet,TokenVerifyView):
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
class UserDetail(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.JWTAuthentication,)

    def get_object(self):
        return self.request.user