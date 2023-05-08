from django.urls import path

from app.apps.core.web import views

urlpatterns = [path("", views.SimpleView.as_view())]
