from django.shortcuts import render


def register(request):
    return render(request, "sign_up_form.html")


def sign_in(request):
    return render(request, "sign_in_form.html")
