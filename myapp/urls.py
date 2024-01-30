from django.urls import path
from .views import index, about, contact, check_result

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('check_result/<str:task_id>/', check_result, name='check_result'),
]