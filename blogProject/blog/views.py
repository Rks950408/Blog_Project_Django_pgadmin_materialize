from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
import math
from .models import Blog

# Create your views here.

def home(req):
    blogs =  Blog.objects.order_by("-date")
    return render(req,'blog/home.html',{'blogs':blogs})

def list(req):
    return render(req,'blog/list.html',{'data':[1,2,3,4,5]})

def about(req):
    return render(req,'blog/about.html')

def details(req,id):
    blog=get_object_or_404(Blog,pk=id)
    return render(req, 'blog/details.html', {'blog': blog})


def evenodd(req):
    return render(req,'blog/Evenodd.html',{'data':[1,2,3,4,5]})

def operations(req):
    data = {'data': [10, 5]}  
    num1, num2 = data['data']
    
    add_result = num1 + num2
    sub_result = num1 - num2
    compare_num=num1>num2
    divide_result = num1 / num2 if num2 != 0 else "Cannot divide by zero!"

    return render(req, 'blog/operations.html', {
        'num1': num1,
        'num2': num2,
        'add_result': add_result,
        'sub_result': sub_result,
        'compare_num':compare_num,
        'divide_result': divide_result
    })

def operations_input(req):
    num1=1
    num2=2
    if req.method == 'POST':
        num1 = int(req.POST['num1'])
        num2 = int(req.POST['num2'])
    # else:
    #     num1, num2 = 10, 5  # Default numbers
    
    add_result = num1 + num2
    sub_result = num1 - num2
    divide_result = num1 / num2 if num2 != 0 else "Cannot divide by zero!" 

    return render(req, 'blog/operation2.html', {
        'num1': num1,
        'num2': num2,
        'add_result': add_result,
        'sub_result': sub_result,
        'divide_result': divide_result
    })

def factorial(req):
    if req.method == 'POST':
        num = int(req.POST['num'])
        # Calculate factorial
        if num < 0:
            factorial_result = "Factorial is not defined for negative numbers."
        else:
            factorial_result = math.factorial(num)
    else:
        num = None
        factorial_result = None

    return render(req, 'blog/factorial.html', {
        'num': num,
        'factorial_result': factorial_result
    })
