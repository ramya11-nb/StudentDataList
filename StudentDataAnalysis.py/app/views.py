# from django.shortcuts import render,redirect
# from .models import Student

# # Create your views here.
# def index(request):
#     data=Student.objects.all()
#     print(data)
#     context={"data":data}
#     return render(request,"index.html",context)

# def insertData(request):
    
#     if request.method=="POST":
#         name=request.POST.get('name')
#         email=request.POST.get('email')
#         age=request.POST.get('age')
#         gender=request.POST.get('gender')
#         print(name,email,age,gender)
#         query=Student(name=name,email=email,age=age,gender=gender)
#         query.save()
#         return redirect("/")

#     return render(request,"index.html")

# def updateData(request,id):
#     if request.method=="POST":
#         name=request.POST['name']
#         email=request.POST['email']
#         age=request.POST['age']
#         gender=request.POST['gender']
#         print(name,email,age,gender)
#         query=Student(name=name,email=email,age=age,gender=gender)
#         query.save()
#         return redirect("/")

#     d=Student.objects.get(id=id)
#     context={"d":d}
#     return render(request,"edit.html",context)

# def deleteData(request,id):
#     data=Student.objects.all()
#     print(data)
#     context={"data":data}
#     return render(request,"index.html",context)


# def about(request):
#     return render(request,"about.html")

# def contact(request):
#     return render(request,"contact.html")


from django.shortcuts import render, redirect
from .models import Student

def index(request):
    data = Student.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)

def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        query = Student(name=name, email=email, age=age, gender=gender)
        query.save()
        return redirect("/")
    return render(request, "index.html")

def updateData(request, id):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']
        student = Student.objects.get(id=id)
        student.name = name
        student.email = email
        student.age = age
        student.gender = gender
        student.save()
        return redirect("/")
    d = Student.objects.get(id=id)
    context = {"d": d}
    return render(request, "edit.html", context)

def deleteData(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("/")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")











