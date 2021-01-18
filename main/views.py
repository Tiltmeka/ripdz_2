from django.shortcuts import render


def index(request):
    data = {
        'title': 'Начальная страница',
        'values': ['some', 'test'],
        'obj':{
            'car': 'bmw',
            'age': '18'
        }
    }
    return render(request, 'main/index.html', data)


def test1(request):
    return render(request, 'main/about.html')