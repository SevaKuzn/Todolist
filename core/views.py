from django.shortcuts import render
import random

# Create your views here.
def monday(request):
    todo_list = ['Помыть посуду','Сделать домашку','Погулять']
    random.shuffle(todo_list)
    return render(request,'monday.html',{'todo_list':todo_list})

def tuesday(request):
    todo_list = ['Погулять','Поспать','Покушать']
    random.shuffle(todo_list)
    return render(request,'tuesday.html',{'todo_list':todo_list})
