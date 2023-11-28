from django_filters import CharFilter, FilterSet
from .models import Ad


class AdFilterSet(FilterSet):
    """
    Django FilterSet for the Ad model.

    Defines a FilterSet for the Ad model, enabling filtering by the 'title' field
    using a case-insensitive containment lookup.
    """

    title = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Ad
        fields = ('title',)
