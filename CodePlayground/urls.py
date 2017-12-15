"""CodePlayground URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import app.views as apv

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', apv.home_view, name='home'),
    url(r'^about/$', apv.about_view, name='about'),
    url(r'^login/$', apv.login_view, name='login'),
    url(r'^logout/$', apv.logout_view, name='logout'),
    url(r'^demo/maze/$', apv.maze_demo, name='maze_demo'),
    url(r'^demo/snake/$', apv.snake_demo, name='snake_demo'),
    url(r'^hotgames/$', apv.hot_view, name='hot'),
    url(r'^beginner/$', apv.beginner_view, name='beginner'),
    url(r'^intermediate/$', apv.intermediate_view, name='intermediate'),
    url(r'^games/$', apv.games_view, name='games'),
    url(r'^link/$', apv.link_view, name='link'),
    url(r'^ai/$', apv.ai_view, name='ai'),
    url(r'^snake/$', apv.snake_view, name='snake'),
    url(r'^fivechess/$', apv.fivechess_view, name='fivechess'),
    url(r'^advanced/$', apv.advanced_view, name='advanced'),
    url(r'^submission/(?P<pk>\d+)/$', apv.submission_display, name='submission'),
]
