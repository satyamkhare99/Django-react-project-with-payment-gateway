from django.http import JsonResponse

def home(request):
    return JsonResponse({'info':'django react course', 'name': 'Satyam'})

