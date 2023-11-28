from django.shortcuts import get_object_or_404
from django_filters import rest_framework as django_filters
from rest_framework import pagination, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrOwner
from ads.models import Ad, Comment
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer
from .filters import AdFilterSet


class AdPagination(pagination.PageNumberPagination):
    """
        Custom pagination class for the Ad model.
    """

    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows ads to be viewed or edited.
    """

    pagination_class = AdPagination
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_class = AdFilterSet


    def get_queryset(self):
        return Ad.objects.filter(author=self.request.user) if 'me' in self.request.path else Ad.objects.all()

    def get_serializer_class(self):
        return AdDetailSerializer if self.action in ['retrieve', 'create', 'partial_update'] else AdSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):

        permission_classes = []

        if self.action == 'list':
            if 'me' in self.request.path:
                permission_classes = [IsAuthenticated]
            else:
                permission_classes = [IsAuthenticatedOrReadOnly]
        if self.action in ['retrieve', 'create']:
            permission_classes = [IsAuthenticated]
        if self.action in ['partial_update', 'destroy']:
            permission_classes = [IsAdminOrOwner]

        return [permission() for permission in permission_classes]


class CommentViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows comments to be viewed or edited.
    """

    pagination_class = AdPagination
    serializer_class = CommentSerializer

    def get_queryset(self):
        ad_pk = self.kwargs.get('ad_pk')
        ad = get_object_or_404(Ad, pk=ad_pk)
        return Comment.objects.filter(ad=ad)

    def get_permissions(self):

        permission_classes = []

        if self.action in ['list', 'create', 'retrieve']:
            permission_classes = [IsAuthenticated]
        if self.action in ['partial_update', 'destroy']:
            permission_classes = [IsAdminOrOwner]

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        ad_pk = self.kwargs.get('ad_pk')
        ad = get_object_or_404(Ad, pk=ad_pk)
        serializer.save(ad=ad, author=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=self.kwargs.get('ad_pk'))
        comment = get_object_or_404(Comment, pk=self.kwargs.get('pk'), ad=ad)
        serializer = self.get_serializer(comment)
        return Response(serializer.data)









