from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_POST
from django.utils.decorators import method_decorator

from django.views import View
import requests


# Create your views here.
def num(request, n):
    isEven = n % 2 == 0
    return render(request, "sample.html", {"n": n, "isEven": isEven})


def record(request, name, age):
    return HttpResponse(f"Name = {name} and age = {age}")

def json_users(request):
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        data = response.json()
    except requests.RequestException as e:
        return JsonResponse({"error": "Failed to fetch data"}, status=500)

    return JsonResponse(data, safe=False)

def json_single_user(request, id):
    try:
        response = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}")
        data = response.json()
    except requests.RequestException as e:
        return JsonResponse({"error": "Failed to fetch data"}, status=500)

    return JsonResponse(data, safe=False)

@csrf_exempt
# @require_http_methods(['GET','POST'])
@require_POST
def show(request):
    return HttpResponse("done " + request.method)


@method_decorator(csrf_exempt, name="dispatch")
class UserView(View):
    def get(self, request):
        return JsonResponse({"message": "This is GET Call"})

    def post(self, request):
        return JsonResponse({"message": "This is POST Call"})

    def put(self, request):
        return JsonResponse({"message": "This is PUT Call"})

    def patch(self, request):
        return JsonResponse({"message": "This is PATCH Call"})

    def delete(self, request):
        return JsonResponse({"message": "This is DELETE Call"})

@method_decorator(csrf_exempt, name="dispatch")
class UserDetailView(View):
    def get(self, request, id):
        if(id>20):
            raise Http404("User not found")
        return JsonResponse({"message": f"This is GET Call for {id}"})
    
    def put(self, request, id):
        return JsonResponse({"message": f"This is PUT Call for {id}"})

    def patch(self, request, id):
        return JsonResponse({"message": f"This is PATCH Call for {id}"})

    def delete(self, request, id):
        return JsonResponse({"message": f"This is DELETE Call for {id}"})