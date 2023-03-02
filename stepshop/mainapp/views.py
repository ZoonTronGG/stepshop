from django.shortcuts import render


# Create your views here.
def products(request):
    title = 'продукты/каталог'

    context = {
        'title': title,
    }

    return render(request, 'products.html', context)
