from django.urls import path
from django.contrib.auth import views as auth_views
from account import views

app_name = 'account'

urlpatterns = [
    # path('login/', views.user_login, name='login')
    # as_view()를 사용한 클래스 기반뷰로 변경
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'), #get방식 함수로 해결
    path('', views.dashboard, name='dashboard'),
]