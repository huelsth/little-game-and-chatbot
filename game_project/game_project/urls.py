from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('game/', include('game.urls')),
    path('chatbot/', include('chatbot.urls')),
    path('', lambda request: HttpResponseRedirect('/game/')),  
]
