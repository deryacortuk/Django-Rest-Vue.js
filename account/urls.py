from django.urls import path, include
from account.views import index, LoginViewSet, RegisterViewSet,  LogoutViewSet,RefreshViewSet,DecoratedTokenObtainPairView,DecoratedTokenRefreshView,DecoratedTokenVerifyView, UserDetail

from rest_framework import routers

app_name ="account"
router = routers.SimpleRouter()
router.register(r"register", RegisterViewSet, basename="register")
router.register(r'login', LoginViewSet, basename='login')
router.register(r"logout", LogoutViewSet, basename="logout")
router.register(r'refresh', RefreshViewSet, basename='refresh')
router.register(r'token', DecoratedTokenObtainPairView, basename='token_pair')
router.register(r'tokenrefresh', DecoratedTokenRefreshView, basename='token_refresh')
router.register(r"verify", DecoratedTokenVerifyView, basename="token_verify")

urlpatterns = [
    path("",index, name="home"),
    path('auth/', include(router.urls)),
     path("user/", UserDetail.as_view(), name="user"),
    
]