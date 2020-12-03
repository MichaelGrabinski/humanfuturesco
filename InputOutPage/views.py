from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from InputOutPage.models import Queries

# Create your views here.


def index(request):
    questions=None
    if request.GET.get('search'):
        search = request.GET.get('search')
        questions = Queries.objects.filter(query__icontains=search)

        name = request.GET.get('name')
        query = Queries.object.create(query=search, user_id=name)
        query.save()

    return render(request, 'InputOutPage/index.html',{
        'questions': questions,
    })