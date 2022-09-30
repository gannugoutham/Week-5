from django.http import JsonResponse

def indexPage(request):
    data = {"message" : "Hello World!"}
    return JsonResponse(data)

# Create your views here.
