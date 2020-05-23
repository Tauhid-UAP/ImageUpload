from django.shortcuts import render
from .models import Photo
from django.core.paginator import Paginator

# Create your views here.

def view_gallery(request):
    context = {}

    photo_list = Photo.objects.all()

    paginator = Paginator(photo_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['page_obj'] = page_obj

    return render(request, 'gallery/view_gallery.html', context)

