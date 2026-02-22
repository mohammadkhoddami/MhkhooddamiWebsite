from django.urls import path, re_path
from django.views.generic import TemplateView

from .views import BlogDetailView, BlogListView, ResumeView, PortfolioDetail, PortfolioList


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    re_path(
        r'^blog/(?P<slug>[\u0600-\u06FF0-9_-]+)/$',
        BlogDetailView.as_view(),
        name='blog_detail'
    ),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('resume/', ResumeView.as_view(), name='resume'),
    path('contact/', TemplateView.as_view(template_name='contacts.html'), name='contact'),
    path('portfolio/', PortfolioList.as_view(), name='portfolio'),
    re_path(
        r'^port/(?P<slug>[\w\u0600-\u06FF\-]+)/$',
        PortfolioDetail.as_view(),
        name='portfolio-detail'
    ),
]
