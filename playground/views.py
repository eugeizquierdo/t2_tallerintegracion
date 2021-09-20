from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Ligas
from django.http import JsonResponse

# Create your views here.

def say_hello(request):
    return render(request, 'hello.html')

class LigasListView(View):
    def get(self, request):
        list = Ligas.objects.all()
        return JsonResponse(list, False)

    # def post(self, request):
    #     # post...
    # def put(self, request):
    #     # put...
    # def delete(self, request):
    #     # delete...

class LigasDetailView(View):
    def get(self, request, pk):
        list = Ligas.objects.get(pk=pk)
        return JsonResponse(list, False)

    # def post(self, request):
    #     # post...
    # def put(self, request):
    #     # put...
    # def delete(self, request):
    #     # delete...