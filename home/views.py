from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View

from .models import (
    Article,
    About,
    Education,
    Experience,
    Skill,
    Portfolio
)

class BlogListView(ListView):
    model = Article
    template_name = 'blog.html'
    context_object_name = 'articles'
    ordering = '-created'


class BlogDetailView(DetailView):
    model = Article
    template_name = "blog_inner.html"
    context_object_name = "article"
    slug_field = "slug"
    slug_url_kwarg = "slug"


class ResumeView(View):
    def get(self, request):
        about = About.objects.first()
        education = Education.objects.all()
        experience = Experience.objects.all()
        skill = Skill.objects.all()
        
        context = {
            "about": about,
            'educations': education,
            'experiences': experience,
            'skills': skill
        }
        
        return render(request, 'resume.html', context)
    

class PortfolioList(ListView):
        model = Portfolio
        template_name = 'portfolio.html'
        context_object_name = 'portfolios'
        ordering = '-created'

class PortfolioDetail(DetailView):
        model = Portfolio
        template_name = "portfolio-detail.html"
        context_object_name = "portfolio"
        slug_field = "slug"
        slug_url_kwarg = "slug"