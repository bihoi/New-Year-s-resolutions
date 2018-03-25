from .models import YourResolutions
from django.shortcuts import render
from django.http import Http404

def index(request):
    all_results = YourResolutions.objects.all()
    context = {
        'all_results': all_results,
    }

    return render(request, 'resolution/index.html', context)

def detail(request, user_id):
    try:
        user = YourResolutions.objects.get(id=user_id)
    except YourResolutions.DoesNotExist:
        raise Http404('Result does not exist')
    return render(request, 'resolution/detail.html', {'user':user})
