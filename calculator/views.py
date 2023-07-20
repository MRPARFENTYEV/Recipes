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
    },
# можете добавить свои рецепты ;)
}
# context_omlet = DATA['omlet']
# context_pasta = DATA['pasta']
# CONTENT = [str(i) for i in range(3)]

def omlet(request):

    context = {'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    }}

    return render(request, 'calculator/omlet.html',context)
    # return render(request, 'calculator/index.html', DATA)
# def pagi(request):
#     paginator = Paginator(CONTENT, 1)
#     page = paginator.get_page(1) # тут надо добраться до ингридиентов
#     context = {
#         'recipe':{{
#         'ingredient1': amount1,
#         'ingredient2': amount2,
#         'ingridient3': amount3
#         }
#     }
#     return render(request,'calculator/index.html', context)
#     # page_num = int(request.Get.get("page", 1))



# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
