from django.core.paginator import Paginator
from django.http import HttpResponse, request
from django.shortcuts import render
import request
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
# ['http:', '', '127.0.0.1:8000', 'omlet', '']
def omlet(request):
    response = str(request).split('/')
    print(response)
    # res = int(request).split('/')
    dish_response_title = response[1]
    pn = int(response[2].split('=')[1].split("'")[0])
    # pn = int(pn[10:])
    # ["<WSGIRequest: GET '", 'omlet', "?servings=4'>"]
    context = {}
    # person_num = pn
    # servings = dish_response_title
    for dish_title, dish_ingridienst_amount in DATA.items():
        if dish_title == dish_response_title:
            context[dish_title] = {}
            for ingridients, amount in dish_ingridienst_amount.items():
                total_amount = amount * pn
                context[dish_title][ingridients] = total_amount
        else:
            pass
    return render(request, 'calculator/index.html', context)

#         else:
#             pass
# def omlet(request):
#     context = {}
#     person_num = 5
#     for dish_title,dish_ingridienst_amount in DATA.items():
#         for ingridients,amount in dish_ingridienst_amount.items():
#             total_amount = amount * person_num
#             context[ingridients] = total_amount
#     return render(request, 'calculator/omlet.html', context)



# response ='http://127.0.0.1:8000/omlet/'.split('/')
# res = 'http://127.0.0.1:8000/omlet/?servings=7'.split('/')
# dish_response_title = response
# print(dish_response_title)
# pn = res[-1]
# pn = int(pn[10:])
# # print(pn)
# # print(type(pn))
# context = {}
# # person_num = pn
# servings = dish_response_title
# for dish_title,dish_ingridienst_amount in DATA.items():
#     if dish_title == servings:
#         context[dish_title] ={}
#         for ingridients,amount in dish_ingridienst_amount.items():
#             total_amount = amount * pn
#             context[dish_title][ingridients] = total_amount
#     else:
#         pass
#
# print(context)


# def product_list(request):
#     products = DATA
#     return  HttpResponse(products)






# context = {}
# person_num = 5
# dish_name ='buter'
# # page_title = request.GET.get('servings',1)
# for dish_title,dish_ingridienst_amount in DATA.items():
#     context[dish_title] ={}
#     for ingridients,amount in dish_ingridienst_amount.items():
#         total_amount = amount * person_num
#         context[dish_title][ingridients] = total_amount


# context = {}
# person_num = 5
# for dish_title,dish_ingridienst_amount in DATA.items():
#     for ingridients,amount in dish_ingridienst_amount.items():
#         total_amount = amount * person_num
#         context[ingridients] = total_amount




# for dish, ingredients in DATA.items():
#     context[dish] = {}
#     for name, quantity in ingredients.items():
#         context[dish][name] = quantity
#
# print(context)
# print(DATA['pasta'])

# def sum(request, op1, op2):
#     result = op1 + op2
#     return HttpResponse(f'Sum = {result}')

context = {}
for recipe, value in DATA.items():
    context[recipe] = value
# print(context)

# for k,v in context.items():
#     for ingr,amount in v.items():


# def pasta(request):
#     servings = int(request.GET.get('servings',1))
#     # transitional_dict = {}
#     context = {}
#     # am = 6
#     omlet_ingridients = {}
#     pasta_ingridients = {}
#     buter_ingridients = {}
#     one = []
#     two = []
#     three = []
#     for k, v in DATA.items():
#         for ingr, amount in v.items():
#             amount =int(amount) * servings
#
#             if k not in one:
#                 one.append(k)
#             two.append(ingr)
#             three.append(amount)
#     # print(one)
#     for food in two[0:3]:
#         for num in three[0:3]:
#             omlet_ingridients[food] = num
#
#     for food_pasta in two[3:5]:
#         for num_pasta in three[3:5]:
#             pasta_ingridients[food_pasta] = num_pasta
#
#     for food_buter in two[5:]:
#         for num_buter in three[5:]:
#             buter_ingridients[food_buter] = num_buter
#
#     context['omlet'] = omlet_ingridients
#     context['pasta'] = pasta_ingridients
#     context['buter'] = buter_ingridients
#     return render(request, 'calculator/pasta.html', context)
# def pasta(request):
#     return render(request, 'calculator/pasta.html', context)
#
#
# def omlet(request):
#     return render(request, 'calculator/omlet.html', context)
# #
# def buter(request):
#     return render(request, 'calculator/buter.html', context)


