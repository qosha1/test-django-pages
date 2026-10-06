from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html")


def pricing(request):
    plans = [("Starter", "$0"), ("Team", "$29"), ("Business", "$99")]
    return render(request, "pages/pricing.html", {"plans": plans})


def faq(request):
    return render(request, "pages/faq.html")
