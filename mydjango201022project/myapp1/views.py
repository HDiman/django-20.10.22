from django.shortcuts import render
from myapp1.models import Worker

# Create your views here.
def index_page(request):
    all_workers = Worker.objects.all()
    print(all_workers)

    workers_filter = Worker.objects.filter(salary=100000)
    print(workers_filter)

    return render(request, 'index.html')


def about_page(request):
    return render(request, 'about.html')
