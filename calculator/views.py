from django.core.paginator import Paginator
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    }}

context = {}
for recipe, value in DATA.items():
    context[recipe] = value
print(context)
# for val in DATA.values():
    # context = {'recipe': val}

def pasta(request):
     return render(request, 'calculator/pasta.html', context)


def omlet(request):
    return render(request, 'calculator/omlet.html', context)

def buter(request):
    return render(request, 'calculator/buter.html', context)


