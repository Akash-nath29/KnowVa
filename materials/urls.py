from django.urls import path, include
from .views import home, material_list, upload_material, material_detail, like_material, dislike_material
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", home, name="home"),
    path('materials/', material_list, name='material-list'),
    path("materials/upload/", upload_material, name="upload-material"),
    path("materials/<int:pk>/", material_detail, name="material-detail"),
    # path("material/<int:pk>/view-pdf/", material_pdf_view, name="material-pdf-view"),
    path('materials/<int:material_id>/like/', like_material, name='like-material'),
    path('materials/<int:material_id>/dislike/', dislike_material, name='dislike-material'),
    path("users/", include("users.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)