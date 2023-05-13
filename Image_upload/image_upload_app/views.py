from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ImageUploader


# Create your views here.
def upload_image(request):
    if request.method == 'POST' and len(request.FILES) != 0:
        image_uploader_obj = ImageUploader()
        image_uploader_obj.photo = request.FILES['image']
        image_uploader_obj.save()
        
    all_images = ImageUploader.objects.all()
    
    return render(request=request, template_name="home.html", context={'img': all_images})


def delete_image(request, image_id):
    if request.method == 'POST':
        obj = ImageUploader.objects.get(pk=image_id)
        obj.delete()
        # In HttpResponseRedirect take the 'route' of the urls.py file
        return HttpResponseRedirect(redirect_to='/')