from . import views
from django.urls import path, include

urlpatterns = [
    path('home/', views.dashboard, name='docs-home'),
]