from django.shortcuts import render
from myapp1.models import Worker

# Create your views here.
def index_page(request):

    # new_worker = Worker(name='Иван', last_name='Иванов', salary=70000)
    # new_worker.save()

    # updating_worker = Worker.objects.get(id=5)
    # print(updating_worker)
    # updating_worker.last_name = 'Кирилов'
    # updating_worker.name = "Сергей"
    # updating_worker.save()

    all_workers = Worker.objects.all()
    # print(all_workers)

    # Filtering some data
    # workers_filter = Worker.objects.filter(salary=100000)
    # print(workers_filter)

    # Delete some data
    # delete_worker = Worker.objects.get(id=3)
    # delete_worker.delete()

    for i in all_workers:
        print(f'Имя: {i.name}, Фамилия: {i.last_name}, Зарплата: {i.salary}, Поряд.номер: {i.id}')

    return render(request, 'index.html')


def about_page(request):
    return render(request, 'about.html')
