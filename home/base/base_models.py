from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field



class TimeStampMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class SluggedMixinModel(TimeStampMixin):
    title = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=255,
        unique=True,
        allow_unicode=True,
        blank=True
    )
    
    class Meta:
        abstract=True
        
    def save(self, *args, **kwargs):
        if not self.slug or self.title:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
        

class BaseSeoModel(SluggedMixinModel):
    
    #Seo Fields
    meta_title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="این عنوان در نتایج گوگل نمایش داده می‌شود. (حدود ۶۰ کاراکتر)"
    )
    
    meta_description = models.TextField(
        blank=True,
        null=True,
        help_text="این متن زیر عنوان در نتایج گوگل می‌آید. (حدود ۱۶۰ کاراکتر)"
    )
    
    og_image = models.ImageField(
        upload_to="seo/og/",
        blank=True,
        null=True,
        help_text="تصویری که هنگام اشتراک‌گذاری لینک نمایش داده می‌شود. (نسبت ۱.۹۱:۱)")


    canonical_url = models.URLField(
        blank=True,
        null=True,
        help_text="اگر این صفحه کپی صفحه‌ی دیگری است، آدرس آن را وارد کنید."
    )
    
    robots_index = models.BooleanField(
        default=True,
        help_text=("اگر تیک نخورده باشد، به موتورهای جستجو می‌گوید این صفحه را ایندکس نکنند (noindex).")    
        )
    
    robots_follow = models.BooleanField(
        default=True,
        help_text="اگر تیک نخورده باشد، به موتورهای جستجو می‌گوید لینک‌های این صفحه را دنبال نکنند (nofollow)."
    )
    
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    alt_image = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        abstract = True