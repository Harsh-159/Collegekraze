from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from Main.forms import SignUpForm
from django.core.mail import send_mail

def Home(request):
    return render(request,"index.html")


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            their_email=form.cleaned_data.get('email')
            send_mail(
                'Thanks for joing our community',
                'We are glad to welcome you to our community and  hope we can make your college experience better.For any confusion or issue feel free to contace us via gmail.',
                'crazecollege@gmail.com',
                [their_email],
                fail_silently=False,
                        )
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    print(form)
    return render(request, 'registration/signup.html', {'form': form})
