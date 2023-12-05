from rest_framework import serializers
from .models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    """
        Serializer for the Comment model.
    """

    author_id = serializers.ReadOnlyField(source='author.id')
    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')
    ad_id = serializers.ReadOnlyField(source='ad.id')

    author_image = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('pk', 'text', 'author_id', 'created_at', 'author_first_name', 'author_last_name',
                  'ad_id', 'author_image')

    def get_author_image(self, instance):
        return instance.author.image if instance.author.image else None


class AdSerializer(serializers.ModelSerializer):
    """
        Serializer for the Ad model.
    """

    price = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False)
    class Meta:
        model = Ad
        fields = ('pk', 'image', 'title', 'price', 'description')


class AdDetailSerializer(serializers.ModelSerializer):
    """
        Serializer for detailed information of the Ad model.
    """

    author_id = serializers.ReadOnlyField(source='author.id')
    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')

    phone = serializers.SerializerMethodField()

    price = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False)

    class Meta:
        model = Ad
        fields = ('pk', 'image', 'title', 'price', 'phone', 'description',
                  'author_first_name', 'author_last_name', 'author_id')

    def get_phone(self, instance):
        return str(instance.author.phone)

