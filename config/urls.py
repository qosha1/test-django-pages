from django.urls import path

from pages import views

urlpatterns = [
    path("", views.home, name="home"),
    path("pricing/", views.pricing, name="pricing"),
    path("faq/", views.faq, name="faq"),
]
