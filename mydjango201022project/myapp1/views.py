from django.shortcuts import render
from myapp1.models import Worker

# Create your views here.
def index_page(request):
    all_workers = Worker.objects.all()
    print(all_workers)

    # Filtering some data
    workers_filter = Worker.objects.filter(salary=100000)
    print(workers_filter)

    for i in all_workers:
        print(f'Имя: {i.name}, Фамилия: {i.last_name}, Зарплата: {i.salary}, Поряд.номер: {i.id}')

    return render(request, 'index.html')


def about_page(request):
    return render(request, 'about.html')
