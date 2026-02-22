from django.db import models
from django.urls import reverse

from django_ckeditor_5.fields import CKEditor5Field


from .base import BaseSeoModel, TimeStampMixin

class Article(BaseSeoModel):
    content = CKEditor5Field(blank=True, null=True)
    author = models.CharField(max_length=255, default='Arsene Team')
        
    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})
    
    def __str__(self):
        return f'{self.title}'


class Portfolio(BaseSeoModel):
    content = CKEditor5Field(blank=True, null=True)
    url = models.URLField(null=True, blank=True)

        
    def get_absolute_url(self):
        return reverse("portfolio", kwargs={"slug": self.slug})

    def __str__(self):
        return f'{self.title}'


class Education(TimeStampMixin):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class Experience(TimeStampMixin):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}'
  
    
class Skill(TimeStampMixin):
    title = models.CharField(max_length=255)
    percent = models.PositiveSmallIntegerField(default=100)
    
    def __str__(self):
        return f'{self.title}'


class About(TimeStampMixin):
    image = models.ImageField()
    summary = models.TextField()
    cv = models.FileField
    
    def __str__(self):
        return f'{self.summary}'
