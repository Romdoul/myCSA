from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from backend.users import views
from rest_framework.routers import DefaultRouter

app_name = 'api'
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'create_company', views.CompanyViewSet)

urlpatterns = [
    url(r'^auth/obtain_token/$', obtain_jwt_token),
    url(r'^auth/refresh_token/$', refresh_jwt_token),
    url(r'all_users/$', views.UserView.as_view(), name='displayAllUsers'),
    url(r'^create_users/$', views.create_user, name='createUser'),
    url(r'^create_company/$', views.create_company, name='createCompany'),
    url(r'^register/$', views.UserRegistration.as_view(), name=''),
    url(r'^display_companies/$', views.DisplayCompanyView.as_view()),
    url(r'^display_user_profile/$', views.DisplayUserProfileView.as_view())
]
