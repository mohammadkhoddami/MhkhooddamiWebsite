from django.db import models
from django.urls import reverse

from django_ckeditor_5.fields import CKEditor5Field


from .base import BaseSeoModel

class Article(BaseSeoModel):
    content = CKEditor5Field(blank=True, null=True)
    author = models.CharField(max_length=255, default='Arsene Team')
        
    def get_absolute_url(self):
        return reverse("article:article_detail", kwargs={"slug": self.slug})


class Portfolio(BaseSeoModel):
    content = CKEditor5Field(blank=True, null=True)
    url = models.URLField(null=True, blank=True)
