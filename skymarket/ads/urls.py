from django.urls import include, path
from .views import AdViewSet, CommentViewSet
from .apps import SalesConfig

app_name = SalesConfig.name

urlpatterns = [
    # Ad URLs
    path('api/ads/', AdViewSet.as_view({'get': 'list', 'post': 'create'}), name='ad-list-create'),
    path('api/ads/me/', AdViewSet.as_view({'get': 'list'}), name='ad-my'),
    path('api/ads/<int:pk>/', AdViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update',
                                             'delete': 'destroy'}), name='ad-detail'),

    # Comment URLs
    path('api/ads/<int:ad_pk>/comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment-list-create'),
    path('api/ads/<int:ad_pk>/comments/<int:pk>/', CommentViewSet.as_view(
        {'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='comment_detail')

]
