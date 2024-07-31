from django.shortcuts import render, HttpResponse, redirect
from .models import *
from costumerapp.models import *
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import *
from .filters import ProductFilter
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import DetailView
from django.views import View


# def homepage(request):
#     # SELECT * FROM Product;
#     product_list = Product.objects.all()
#     filter_object = ProductFilter(
#         data=request.GET,
#         queryset=product_list
#     )
#
#     context = {"filter_object": filter_object}
#     # return HttpResponse("Hello Django!")
#     return render(request, 'index.html', context)


# def user_lst(request):
#     user_lst = User.objects.all()
#     context = {"user_lst": user_lst}
#     return render(request, 'user_lst.html', context)
#
#
# def user_detail(request, id):
#     user_info = User.objects.get(id=id)
#     context = {"user": user_info}
#     # if request.method == "GET":
#     return render(request, 'user_detail.html', context)


# def user_cabinet(request, id):
#     user = User.objects.get(id=id)
#     context = {"user": user}
#     return render(request, 'cabinet.html', context)



# def product_detail(request, id):
#     # SELECT * FROM Product WHERE id = $id; -- где id - число с url
#     product_object = Product.objects.get(id=id)
#
#     # Увеличение просмотра
#     product_object.views_qty += 1
#
#     # Уникальные просмотры
#     if request.user.is_authenticated:
#         user = request.user
#         if not Costumer.objects.filter(user=user).exists():
#             costumer = Costumer.objects.create(
#                 name=user.username,
#                 age=0,
#                 gender='-',
#                 user=user,
#             )
#         costumer = user.costumer
#         product_object.costumer_views.add(costumer)
#         # product_object.costumer_views.add(request.user.costumer)
#
#     # Сохранение в БД
#     product_object.save()
#
#     context = {
#         "product": product_object,
#     }
#     return render(request, 'product_detail.html', context)
#
#
# def product_create(request):
#     context = {}
#     context["product_form"] = ProductForm()
#
#     if request.method == "GET":
#         return render(request, 'product_create.html', context)
#     if request.method == "POST":
#         product_form = ProductForm(request.POST, request.FILES)
#         if product_form.is_valid():
#             product_form.save()
#             messages.success(request, "Вы успешно создали товар")
#             return redirect('/')
#         return HttpResponse("Ошибка валидации!")
#
#
# def product_update(request, id):
#     context = {}
#     product_object = Product.objects.get(id=id)
#     context["product_form"] = ProductForm(instance=product_object)
#
#     if request.method == "GET":
#         return render(request, 'product/update.html', context)
#     if request.method == "POST":
#         product_form = ProductForm(request.POST, request.FILES, instance=product_object)
#         if product_form.is_valid():
#             product_form.save()
#             messages.success(request, "Вы успешно обновили")
#             return redirect('/')
#     return HttpResponse("Ошибка валидации!")


# def search(request):
#     keyword = request.GET["keyword"]
#     # LIKE
#     products = Product.objects.filter(
#         Q(name__icontains=keyword) |
#         Q(category__name__icontains=keyword)
#     )
#     context = {"products": products}
#     return render(request, 'search_result.html', context)
#
#
# def registration(request):
#     context = {}
#
#     if request.method == "POST":
#         reg_form = RegistrationForm(request.POST)
#         if reg_form.is_valid():
#             user_object = reg_form.save()
#             password = request.POST["password"]
#             user_object.set_password(password)
#             user_object.save()
#             return redirect('/')
#         return HttpResponse("Ошибка валидации")
#
#     reg_form = RegistrationForm()
#     context["reg_form"] = reg_form
#     return render(request, "start/registration.html", context)
#
#
# def signin(request):
#     context = {}
#
#     if request.method == "POST":
#         form = AuthForm(request.POST)
#         if form.is_valid():
#             username = request.POST["username"]
#             password = request.POST["password"]
#             user = authenticate(
#                 request,
#                 username=username,
#                 password=password,
#             )
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, "Вы успешно авторизовались")
#                 return redirect('/')
#             messages.warning(request, "Логин и/или пароль неверны")
#
#
#     form = AuthForm()
#     context["form"] = form
#     return render(request, "start/signin.html", context)
#
#
# def signout(request):
#     logout(request)
#     return redirect('/')


