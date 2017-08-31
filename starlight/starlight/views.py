from django.http import HttpResponse

# Create your views here.
def indexView(request):
	return HttpResponse("This is the home page")

def galleryView(request):
	return HttpResponse("This is the gallery")
