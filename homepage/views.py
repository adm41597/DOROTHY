from django.shortcuts import render

def homepage(request):
    #if request.method == 'GET':
    return render(request, 'homepage.html')
