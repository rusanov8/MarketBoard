from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User


class Ad(models.Model):
    """
    Model representing an advertisement
    """

    title = models.CharField(db_index=True, max_length=255, verbose_name=_('Title'), )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Price'))
    description = models.TextField(verbose_name=_('Description'), blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, verbose_name=_('Author'), related_name='ads')
    image = models.ImageField(upload_to='ads/', verbose_name=_('Image'), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Date and time of creation'))

    class Meta:
        verbose_name = 'ad'
        verbose_name_plural = 'ads'
        db_table = 'ads'
        ordering = ('-created_at',)


class Comment(models.Model):
    """
    Model representing an comment
    """

    text = models.TextField(verbose_name=_('Text'))
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name=_('Author'), related_name='comments')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name=_('Ad'), related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Date and time of creation'))

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        db_table = 'comments'
        ordering = ('-created_at',)
