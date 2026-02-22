from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('blog_inner/', TemplateView.as_view(template_name='blog_inner.html'), name='blog_detail'),
    path('blog/', TemplateView.as_view(template_name='blog.html'), name='blog'),
    path('resume/', TemplateView.as_view(template_name='resume.html'), name='resume'),
    path('contact/', TemplateView.as_view(template_name='contacts.html'), name='contact'),
    path('portfolio/', TemplateView.as_view(template_name='portfolio.html'), name='portfolio'),

]
