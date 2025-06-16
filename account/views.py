from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from account.forms import RegisterForm, LoginForm, MyAccountForm    
from django.contrib.auth import login as django_login, logout as django_logout, authenticate
from django.contrib.auth.decorators import login_required
from order.models import Order
# Create your views here.
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from account.tokens import account_activation_token
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
User = get_user_model()

def login(request):
    loginform = LoginForm
    registerform = RegisterForm



    if request.method == 'POST':
        form = RegisterForm(data = request.POST)
        print(request.POST)
        if form.is_valid():
            user = form.save(False)
            current_site = get_current_site(request)
            subject = 'Activate Your Mioca Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect(reverse_lazy('login'))
        


    if request.method == 'POST':
        next = request.GET.get('next', reverse_lazy('home'))
        form = LoginForm(data = request.POST)
        print(request.POST)
        if form.is_valid():
            user = authenticate(request, username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if not user:
                pass
            else:
                django_login(request, user)
                return redirect(next)




    context = {
        'registerform': registerform,
        'loginform' : loginform
    }
    return render(request, 'login.html', context)


@login_required(login_url='login')
def myAccount(request):
    form = MyAccountForm
    orders = Order.objects.filter(user=request.user)
    if request.method == "POST":
        form = MyAccountForm(data = request.POST, instance = request.user)
        if form.is_valid():
            form.save()
    context = {
        'form': form,
        'orders': orders
    }
    return render(request, 'my-account.html', context)

def logout(request):
    django_logout(request)
    return redirect(reverse_lazy('home'))

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        django_login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')