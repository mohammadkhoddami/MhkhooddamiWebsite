from django.contrib import admin
from .models import Article, Portfolio, Education, Experience, Skill, About


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('author',)
    search_fields = ('title', 'author', 'content')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('title', 'slug', 'author', 'content')
        }),
        ('سئو', {
            'classes': ('collapse',),
            'fields': ('seo_title', 'seo_description', 'seo_keywords')
        }),
        ('تاریخ‌ها', {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('title', 'slug', 'url', 'content')
        }),
        ('سئو', {
            'classes': ('collapse',),
            'fields': ('seo_title', 'seo_description', 'seo_keywords')
        }),
        ('تاریخ‌ها', {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('title', 'start', 'end', 'created_at')
    search_fields = ('title', 'summary')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('title', 'summary', 'start', 'end')
        }),
        ('تاریخ‌ها', {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'start', 'end', 'created_at')
    search_fields = ('title', 'summary')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('title', 'summary', 'start', 'end')
        }),
        ('تاریخ‌ها', {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'percent', 'created_at')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('title', 'percent')
        }),
        ('تاریخ‌ها', {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('image', 'summary', 'cv')
        }),
        ('تاریخ‌ها', {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )

    def has_add_permission(self, request):
        # فقط یک رکورد About مجاز است
        return not About.objects.exists()