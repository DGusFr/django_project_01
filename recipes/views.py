from django.shortcuts import render


# HttpResponse é a resposta ao request
def home(request):
    # return HttpResponse('HOME')
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Diego',
    })


def recipe(request, id):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Luiz Otávio',
    })
