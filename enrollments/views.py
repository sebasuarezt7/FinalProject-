from django.shortcuts import render

def enrollment_list(request):
    return render(request, "enrollments/enrollment_list.html")