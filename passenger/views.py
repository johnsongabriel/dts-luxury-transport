from django.shortcuts import render

# Create your views here.
def homePage(request):
    return render(request, 'passenger/index.html')

def galleryPage(request):
    return render(request, 'passenger/gallery.html')