from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from .forms import TaskForm
from .models import Todo
from json import loads
def todolist(request):
    message="Admin" if request.user.is_superuser else "Guest"
    if request.method == "POST": #проверяем то что метод именно POST
        print(request.POST)
        print(request.method==None)
       
        if "Add" in request.POST: #Добавляем задание если есть Add
            ToDoForm=TaskForm(request.POST)
            if ToDoForm.is_valid():
                todo=Todo.objects.create(
                    name = ToDoForm.cleaned_data["name"],
                    email = ToDoForm.cleaned_data["email"],
                    status = ToDoForm.cleaned_data["status"],
                    text = ToDoForm.cleaned_data["text"]
                    )
                todo.save()
                message='Added successfully'
                return redirect('/')
            else:
                message='Invalid form'
        elif "login" in request.POST: #Аутентификация если есть login
            user = authenticate(username=request.POST['Login'],
                                password=request.POST['Password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    message='Disabled account'
            else:
                message='Invalid login or password'
        elif "logout" in request.POST: #Выход если есть logout
            logout(request)
            message='Logged Out Successfully'
        elif request.POST=={}: #Редактирование
            body = loads(request.body.decode('utf-8'))
            if "id" in body: #Через галочку
                redact = Todo.objects.get(id=body["id"])
                redact.done=True if redact.done==False else False
                redact.save()
            elif "text_id" in body: #Через поле текст
                redact = Todo.objects.get(id=body["text_id"])
                redact.text=body["text"]
                redact.byadmin=True
                redact.done=True
                redact.save()
    cookie = int(request.COOKIES.get('order', 6)) 
    orders=['name','-name','email','-email','status','-status'] #Сортировка
    todos = Todo.objects.order_by(orders[cookie]) if cookie!=6 else Todo.objects.all()
    page = request.GET.get('page', 1) #Пагинация
    paginator = Paginator(todos, 3) 
    try:
        todos = paginator.page(page)
    except PageNotAnInteger:
        todos = paginator.page(1)
    except EmptyPage:
        todos = paginator.page(paginator.num_pages)
    return render(request, "todo.html", {"todos": todos, "message": message})
