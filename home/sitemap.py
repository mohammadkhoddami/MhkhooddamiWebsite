from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Article, Portfolio


class ArticleSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return obj.get_absolute_url()


class PortfolioSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7
    protocol = 'https'

    def items(self):
        return Portfolio.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return obj.get_absolute_url()


class StaticSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 1.0
    protocol = 'https'

    def items(self):
        return ['index', 'portfolio', 'blog', 'about', 'contact']

    def location(self, item):
        return reverse(item)
