from django.urls import path
from . import views


urlpatterns = [
    path(route="", view=views.upload_image, name="upload_image_page"),
    path(route="delete/<int:image_id>", view=views.delete_image, name="delete_data"),
]
