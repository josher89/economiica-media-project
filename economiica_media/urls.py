from django.urls import path

from .views import EconomiicaMediaListCreateView, EconomiicaMediaDeleteView

urlpatterns = [
    path(
        "economiica_media/",
        EconomiicaMediaListCreateView.as_view(),
        name="media-list-create",
    ),
    path(
        "economiica_media/<int:pk>/",
        EconomiicaMediaDeleteView.as_view(),
        name="economiica-list-delete",
    ),
]
