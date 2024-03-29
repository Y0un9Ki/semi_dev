from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from users.forms import SigninForm, SignupForm
from users.models import User

# Create your views here.
def signin_view(request):
    
    if request.user.is_authenticated:
        return redirect('posts/feeds/')
    
    if request.method == 'POST':
        form = SigninForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            
            if user:
                login(request, user)
                return redirect('/posts/feeds/')
            
            else:
                form.add_error(None, '입력한 사용자는 존재하지 않습니다.')
                
        context = {'form':form}
        return render(request, 'users/signin.html', context)
    
    else:
        form = SigninForm()
        context = {'form':form}
        return render(request, 'users/login.html', context)
    
def signout_view(request):
    logout(request)
    return redirect('')

def signup_view(request):
    if request.method =='POST':
        form = SignupForm(data = request.POST)
        if form.is_valid():
            user = form.save()
            
        # if password1 != password2:
        #     form.add_error('password2', '비밀번호가 서로 다릅니다.')
            
        # if User.objects.filter(username=username).exists():
        #     form.add_error('username', '입력한 id는 이미 사용중입니다.')
            
        # if form.errors:
        #     context={'form':form}
        #     return render(request, 'users/signup.html', context)
        # 우리가 form class 안에 함수로 만들어서 검증을 form에서 할 수 있게 만들어 줬다.
        
            login(request, user)
            return redirect('/posts/feeds/')
        
    else:
        form = SignupForm()
        
    context = {'form':form}
    return render(request, 'users/signup.html', context)   
    
    