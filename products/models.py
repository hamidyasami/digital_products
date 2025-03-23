from faulthandler import is_enabled

from django.db import models
from django.utils.translation import gettext_lazy as _




class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,verbose_name=_('parent'))
    title = models.CharField(_('title'),max_length=50)
    description = models.TextField(_('description'),blank=True)
    avatar = models.ImageField(_('avatar'),blank=True,upload_to='categoris/')
    is_enabled = models.BooleanField(_('is_enabled'),default=True)
    create_time = models.DateTimeField(_('create_time'),auto_now_add=True)
    update_time = models.DateTimeField(_('update_time'),auto_now=True)

    class Meta:
        db_table = 'category'
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.title



class Product(models.Model):
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='products/')
    is_enabled = models.BooleanField(_('is_enabled'), default=True)
    categories = models.ManyToManyField('Category', verbose_name=_('categories'),blank=True)
    create_time = models.DateTimeField(_('create_time'), auto_now_add=True)
    update_time = models.DateTimeField(_('update_time'), auto_now=True)

    class Meta:
        db_table = 'product'
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return self.title


class File(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name=_('product'))
    title = models.CharField(_('title'), max_length=50)
    file = models.FileField(_('file'), upload_to='file/%Y/%m/%d')
    is_enabled = models.BooleanField(_('is_enabled'), default=True)
    create_time = models.DateTimeField(_('create_time'), auto_now_add=True)
    update_time = models.DateTimeField(_('update_time'), auto_now=True)

    class Meta:
        db_table = 'file'
        verbose_name = _('file')
        verbose_name_plural = _('files')