from django.shortcuts import render

def professor_dashboard(request):
    return render(request, "professors/dashboard.html")