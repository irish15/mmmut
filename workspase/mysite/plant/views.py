from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import get_user_model
# from django.contrib.auth import login, authenticate
from django.contrib.auth.views import (LoginView, LogoutView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired, loads, dumps
from django.http import Http404, HttpResponseBadRequest
from django.template.loader import render_to_string
from django.views import generic
from . import forms

User = get_user_model()    
def post_list(request):
    form_txt = forms.MyForm()
    form_img = forms.PhotoForm()
    # if request.method == 'GET':
    return render(request, 'plant/post_list.html', {
        'form_txt': form_txt, 
        'form_img': form_img,

    })

#アカウント作成
class Create_account(generic.CreateView):
    def post(self, request, *args, **kwargs):
        form = forms.UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            #フォームから'username'を読み取る
            username = form.cleaned_data.get('username')
            #フォームから'password1'を読み取る
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        return render(request, 'plant/user_create.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = forms.UserCreateForm(request.POST)
        return  render(request, 'plant/user_create.html', {'form': form,})

create_account = Create_account.as_view()

class Top(generic.TemplateView):
    template_name = 'plant/top.html'


class Login(LoginView):
    """ログインページ"""
    form_class = forms.LoginForm
    template_name = 'plant/login.html'
#     def post(self, request, *arg, **kwargs):
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             user = User.objects.get(username=username)
#             login(request, user)
#             return redirect('/')
#         return render(request, 'login.html', {'form': form,})
# 
#     def get(self, request, *args, **kwargs):
#         form = LoginForm(request.POST)
#         return render(request, 'login.html', {'form': form,})
# 
# account_login = Account_login.as_view()    


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'plant/top.html'
# 
# 
# class UserCreate(generic.CreateView):
#     """ユーザー仮登録"""
#     template_name = 'plant/user_create.html'
#     form_class = forms.UserCreateForm
# 
#     def form_valid(self, form):
#         """仮登録と本登録用メールの発行."""
#         # 仮登録と本登録の切り替えは、is_active属性を使うと簡単です。
#         # 退会処理も、is_activeをFalseにするだけにしておくと捗ります。
#         user = form.save(commit=False)
#         user.is_active = False
#         user.save()
# 
#         # アクティベーションURLの送付
#         current_site = get_current_site(self.request)
#         domain = current_site.domain
#         context = {
#             'protocol': self.request.scheme,
#             'domain': domain,
#             'token': dumps(user.pk),
#             'user': user,
#         }
# 
#         subject = render_to_string('plant/mail_template/create/subject.txt', context)
#         message = render_to_string('plant/mail_template/create/message.txt', context)
# 
#         user.email_user(subject, message)
#         return redirect('plant:user_create_done')


# class UserCreateDone(generic.TemplateView):
#     """ユーザー仮登録したよ"""
#     template_name = 'plant/user_create_done.html'
# 
# 
# class UserCreateComplete(generic.TemplateView):
#     """メール内URLアクセス後のユーザー本登録"""
#     template_name = 'plant/user_create_complete.html'
#     timeout_seconds = getattr(settings, 'ACTIVATION_TIMEOUT_SECONDS', 60*60*24)  # デフォルトでは1日以内
# 
#     # def get(self, request, **kwargs):
#     def post(self, request, *args, **kwargs):
#         """tokenが正しければ本登録."""
#         token = kwargs.get('token')
#         try:
#             user_pk = loads(token, max_age=self.timeout_seconds)
# 
#         # 期限切れ
#         except SignatureExpired:
#             return HttpResponseBadRequest()
# 
#         # tokenが間違っている
#         except BadSignature:
#             return HttpResponseBadRequest()
# 
#         # tokenは問題なし
#         else:
#             try:
#                 user = User.objects.get(pk=user_pk)
#             except User.DoesNotExist:
#                 return HttpResponseBadRequest()
#             else:
#                 if not user.is_active:
#                     # 問題なければ本登録とする
#                     user.is_active = True
#                     user.save()
#                     return super().get(request, **kwargs)
# 
#         return HttpResponseBadRequest()        