from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def form(request):
    return render(request,'main/form.html')
def example(request):
    return render(request,'main/example.html')