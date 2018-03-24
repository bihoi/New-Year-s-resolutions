from django.http import HttpResponse
from .models import YourResolutions

def index(request):
    all_results = YourResolutions.objects.all()
    html = ''
    for user in all_results:
        url = '/resolution/'+ str(user.id)+'/'
        html+= '<a href="'+ url +'">'+ user.health +'</a><br>'
    return HttpResponse(html)

def detail(request, user_id):
    return HttpResponse("<h2> Details for user id " + str(user_id)+" </h2>")
