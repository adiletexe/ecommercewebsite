from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.store, name='store_page'),
    path('<slug:slug_id>/', views.store, name='categories'),
    path('<slug:slug_id>/<slug:product_slug>/', views.product_details, name='product_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)