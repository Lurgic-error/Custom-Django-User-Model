from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from .forms import RegisterForm, UserLoginForm
from .models import User
# Create your views here.


class UserCreateView(CreateView):

    form_class = RegisterForm
    template_name = 'accounts/authentication/signup.html'

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return super().form_valid(form)

class UserLoginView(LoginView):

    form_class = UserLoginForm
    template_name = 'accounts/authentication/login.html'

    success_url = 'home'
    # def post(self, request, **kwargs):
    #     print(kwargs)


    def form_valid(self, form):
        """Security check complete. Log the user in."""
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        login(request, user)
        return success_url

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    print(form.cleaned_data.get('email'))
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        print(f'wooozzzaaaa---- {email}')
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "accounts/authentication/login.html", context)



class UserListView(ListView):
    model = User
    template_name = "accounts/account_list.html"


class UserDetailView(DetailView):

    model = User
    # queryset = User.objects.filter(email=request.kwargs.get('email'))
    template_name = 'accounts/account_detail.html'

    # def get_object(self, **kwargs):
    #     email = kwargs.get('email')
    #     object = get_object_or_404(User, email=email)
    #     return object

    def get_queryset(self, **kwargs):

		# if self.request.user.is_authenticated:
	    return User.objects.filter(pk=self.kwargs.get('pk'))
		# else:
		# 	return User.objects.none()


class UserUpdateView(UpdateView):
    model = User
    form_class = RegisterForm
    template_name = "accounts/account_update.html"

    def get_queryset(self, **kwargs):

		# if self.request.user.is_authenticated:
	    return User.objects.filter(pk=self.kwargs.get('pk'))


class UserDeleteView(DeleteView):
    model = User
    template_name = "accounts/account_delete.html"


    def get_queryset(self, **kwargs):

		# if self.request.user.is_authenticated:
	    return User.objects.filter(pk=self.kwargs.get('pk'))

