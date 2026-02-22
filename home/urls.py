from django.urls import path, re_path
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from home.sitemap import ArticleSitemap, PortfolioSitemap, StaticSitemap
from .views import BlogDetailView, BlogListView, ResumeView, PortfolioDetail, PortfolioList




sitemaps = {
    'static': StaticSitemap,
    'articles': ArticleSitemap,
    'portfolios': PortfolioSitemap,
}


urlpatterns = [
    path('', cache_page(60 * 60 * 24)(TemplateView.as_view(template_name='index.html')), name='index'),
    re_path(
        r'^blog/(?P<slug>[\u0600-\u06FF0-9_-]+)/$',
        BlogDetailView.as_view(),
        name='blog_detail'
    ),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('resume/', cache_page(60 * 60 * 12)(ResumeView.as_view()), name='resume'),
    path('contact/', cache_page(60 * 60 * 24)(TemplateView.as_view(template_name='contacts.html')), name='contact'),
    path('portfolio/', PortfolioList.as_view(), name='portfolio'),
    re_path(
        r'^port/(?P<slug>[\w\u0600-\u06FF\-]+)/$',
        PortfolioDetail.as_view(),
        name='portfolio-detail'
    ),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

]
