    from django.urls import path
    from . import views

    urlpatterns = [

        path('', views.hello, name="Swapna"),
        path('add/', views.addition, name="addition"),
        path('about/', views.about, name="about"),
        path('contact', views.contact, name='contact'),
]
