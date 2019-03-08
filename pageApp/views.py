from django.shortcuts import render

# Create your views here.

# route to page 1
def index(request):
    return render(request, 'pageApp/index.html')

# route to page2
def pageTwo(request):
    return render(request, 'pageApp/page2.html')

# route to page3
def pageThree(request):
    return render(request, 'pageApp/page3.html')