"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

from users import views as user_views
from quiz.views import expenses
from dashboard.views import dash_home, dash_home_poor, dash_home_poor2
from quiz.views import expenses, main_quiz, quiz_question, quiz_answer, quiz_finish

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'
    ),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'
    ),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'
    ),
    path('password-reset/done',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'
    ),
    path('dashboard/', dash_home_poor2, name='dashboard_poor'),
    path('dashboard2/', dash_home_poor, name='dashboard_poor'),
    path('', dash_home, name='home'),
    path('quiz/', main_quiz, name='quiz'),
    path('quiz/finish/', quiz_finish, name='quiz_finish'),
    path('quiz/<int:quiz_id>/<int:question_position>/', quiz_question, name='quiz_question'),
    path('quiz/ans/<int:ans_id>/', quiz_answer, name='quiz_answer'),
    path('expenses/', expenses, name='expenses'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
