from django.urls import path
from . import views

urlpatterns = [
    # clients/
    path("", views.index, name="index"),
    path("client/<int:client_id>", views.client_details, name="client_details")
]
