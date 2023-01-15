from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView
from .forms import ImageUploadForm

class ImageUploadView(CreateView):
    template_name = "nippo/image-upload.html"
    form_class = ImageUploadForm
    success_url = "/"