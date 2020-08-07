from django.shortcuts import render

# Create your views here.

def index(request):
    """
    Home page for blogs site
    """
    context = {}
    return render(request, 'ghosts/index.html', context)


def manage_profile(request):
    # if not request.user.is_authenticated:
    context = {}
    return render(request, 'ghosts/manage_profile.html', context)


