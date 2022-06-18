from django.http import JsonResponse

def home(request):
    return JsonResponse({'Info': ' TShirt Shopping Site', 'Name': 'Miki'})
