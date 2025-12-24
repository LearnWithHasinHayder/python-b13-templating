from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def dhaka(request):
    # weather = {"location": "Dhaka", "temperature": "20 degree", "condition": "cold"}
    weather = {"location": "Dhaka", "temperature": 20}
    forecast = ["sunny","rainy","sunny","hot","cold","freezing"]
    # title="Weather App 1.0"
    # return JsonResponse(weather)
    # return render(request, 'common/weather.html',{'weather':weather})
    # return render(request, 'common/conditional.html',{'weather':weather, 'forecasts':forecast, 'title':title})
    return render(request, 'common/conditional.html',{'weather':weather, 'forecasts':forecast})


def rajshahi(request):
    weather = {
        "location": "Rajshahi",
        "temperature": 12,
    }
    forecast = ["cold","rainy","cold","sunny","cold","freezing"]
    title="Weather App 1.0"
    
    # isEven = weather["temperature"] % 2 == 0
    # return JsonResponse(weather)
    # return render(request, 'common/report.html', weather)
    # return render(request, 'common/weather.html', {'weather':weather})
    # return render(request, 'common/conditional.html', {'weather':weather, 'forecasts':forecast, 'title':title})
    return render(request, 'common/conditional.html', {'weather':weather, 'forecasts':forecast})


def intro(request):
    topic = "Django Templating"
    welcome_message = "Welcome to this class!!!"
    return render(request, "simple.html", {"topic": topic, 'message':welcome_message})
