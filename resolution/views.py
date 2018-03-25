from .models import YourResolutions
from django.shortcuts import render, get_object_or_404


def index(request):
    all_results = YourResolutions.objects.all()
    context = {
        'all_results': all_results,
    }

    return render(request, 'resolution/index.html', context)

def detail(request, note_id):
    note = get_object_or_404(YourResolutions, pk=note_id)
    return render(request, 'resolution/detail.html', {'note':note})
