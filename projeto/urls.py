from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


# HttpResponse é a resposta ao request
def my_view(request):
    return HttpResponse("Olá")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("sobre/", my_view),
]
