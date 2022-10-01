from django.db import models
from django.utils.text import slugify

class Developer(models.Model):
    name = models.CharField(max_length=50,null=True)
    age = models.IntegerField(null=True,blank=True)
    skill = models.CharField(max_length=50,null=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        verbose_name = 'Developer'
        verbose_name_plural = 'Developers'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.name)

            has_slug = Developer.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.name) + '-' + str(count) 
                has_slug = Developer.objects.filter(slug=slug).exists()

            self.slug = slug
        super().save(*args, **kwargs)
