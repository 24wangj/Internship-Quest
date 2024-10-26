from django.shortcuts import render

# Create your views here.
def get_list():
    
    pass

def home_page(request):
    return render(request, 'index.html')