from django.urls import path, include


import blogs.views


urlpatterns = [
        path('<int:blog_id>/', blogs.views.detail, name='detail'),

]


















