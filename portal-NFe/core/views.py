from django.contrib.auth            import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models     import User
from django.shortcuts               import render
from django.http                    import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.urls                    import reverse

def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    return  render(request, 'login.html')

def login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            context['erro'] ={'text':'Usuario ou senha invalidos!',
                              'type':'danger'}

    return  render(request, 'login.html', context )

def logout(request):
    auth_logout(request)
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

@login_required
def settings(request, name):
    context = {}

    if str(request.user) != str(name):
        raise Http404

    if request.method == 'POST':
        username   = request.POST.get('username')
        password   = request.POST.get('password')
        email      = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name  = request.POST.get('last_name')
        check      = request.POST.get('check')
        password_n = request.POST.get('new_password')
        password_c = request.POST.get('confirm_password')

        return  render(request, 'settings.html', context)

    return render(request, 'settings.html', context)

def validate_username(request):
    username = request.GET.get('username')

    data = { 'is_taken': User.objects.filter(username__iexact=username).exists() }

    if data['is_taken']:
        data['error_message'] = 'Username já existe!'

    return JsonResponse(data)
