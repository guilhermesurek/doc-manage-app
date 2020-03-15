from django.shortcuts import render
from django.urls import reverse

def menu_view(request):
    context = {
        'menu_options': [
            {
                'name': 'Upload',
                'url': reverse('upload')
             },
             {
                 'name': 'Download',
                 'url': reverse('download')
             }
            ],
    }
    return render(request, 'menu/index.html', context=context)