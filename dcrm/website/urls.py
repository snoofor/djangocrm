"""
URL configuration for dcrm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views

app_name = 'website' # for reverse jinja syntax

    # in order to use django form use below sign up - then signup.html use {{form}} in urlpatterns

    # {% for field in form %}
    # <div class="mb-3"
    #    {{field.label_tag}}
    #    {{field}}
    # </div>
    # {% endfor %}

    # path('signup', views.SignUpView.as_view(), name='signup'), # CBV change class to view by using as_view()

urlpatterns = [
    path('', views.home, name='home'),
    # in order to create your own form use below
    path("signup/", views.signup_user, name="signup"),
]
