from django.urls import path , include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.home , name = 'home'),
    path("category/<slug:val>",views.CategoryView.as_view(), name="category"),
    path("product-detail/<int:pk>", views.ProductDetail.as_view(), name="product-detail"),
    path("category-title/<val>", views.CategoryTitle.as_view(), name="category-title"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
