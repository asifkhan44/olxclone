from django.urls import path
from customer import views

urlpatterns=[
        path('',views.SigninView.as_view(),name='signin'),
        path('signup',views.SignupView.as_view(),name='signup'),
        path('home',views.HomeView.as_view(), name='user-home'),
]