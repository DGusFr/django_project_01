from django.http import HttpResponse
from django.shortcuts import render


# HttpResponse é a resposta ao request
def home(request):
    # return HttpResponse('HOME')
    return render(request, 'recipes/home.html', context={
        'name': 'Diego',
    })
