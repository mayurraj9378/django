from django.urls import include, path
from electronics import views

urlpatterns=[
    path('product/',views.product_detail,name='product_detail'),
]