from django.shortcuts import render


# Create your views here.

def examply_view(request):
    return render(request, "my_app/example.html")


def variable(request):

    return render(request, 'my_app/variable.html')
