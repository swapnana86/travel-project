from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.
def registration(request):
    if request.method == 'POST':
        username_var = request.POST['username']
        password_var = request.POST['password']
        email_var = request.POST['email']
        firstname_var = request.POST['first_name']
        lastname_var = request.POST['last_name']
        user = User.objects.create_user(username=username_var, password=password_var, email=email_var,
                                        first_name=firstname_var, last_name=lastname_var)
        user.save()
        print("registration completed")


    return render(request, 'registration.html')
