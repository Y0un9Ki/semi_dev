from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from users.forms import SigninForm, SignupForm
from users.models import User
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class SignupAPIView(APIView):
    def post(self, request):
        form = SignupForm(data=request.data)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return Response({'message': '회원가입이 성공적으로 완료되었습니다.'})
        else:
            return Response({'error': form.errors}, status=400)
        
class SigninAPIView(APIView):
    def post(self, request):
        form = SigninForm(data=request.data)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return Response({'message': '로그인이 성공적으로 완료되었습니다.'})
            else:
                return Response({'error': '입력한 사용자는 존재하지 않습니다.'}, status=400)
        else:
            return Response({'error': form.errors}, status=400)
        
class SignoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': '로그아웃이 성공적으로 완료되었습니다.'})





# def signin_view(request):
    
#     if request.user.is_authenticated:
#         return redirect('posts/feeds/')
    
#     if request.method == 'POST':
#         form = SigninForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
            
#             user = authenticate(username=username, password=password)
            
#             if user:
#                 login(request, user)
#                 return redirect('/posts/feeds/')
            
#             else:
#                 form.add_error(None, '입력한 사용자는 존재하지 않습니다.')
                
#         context = {'form':form}
#         return render(request, 'users/signin.html', context)
    
#     else:
#         form = SigninForm()
#         context = {'form':form}
#         return render(request, 'users/login.html', context)
    
# def signout_view(request):
#     logout(request)
#     return redirect('')

# def signup_view(request):
#     if request.method =='POST':
#         form = SignupForm(data = request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('/posts/feeds/')
        
#     else:
#         form = SignupForm()
        
#     context = {'form':form}
#     return render(request, 'users/signup.html', context)   
    
    