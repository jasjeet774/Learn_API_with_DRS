from django.http import HttpResponse , JsonResponse
def home_page(requeat):
    friends=["nobita","doremon","sunio"]
    print("home page requested")
    return JsonResponse(friends,safe=False)