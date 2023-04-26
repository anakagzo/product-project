from django.urls import path, include


import accounts.views


urlpatterns = [
        path('create', accounts.views.create_acc, name='create_acc'),
        path('<int:product_id>/', accounts.views.pro_detail, name='pro_detail'),
    ]