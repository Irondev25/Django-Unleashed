from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=31)
    slug = models.SlugField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('organizer_tag:detail', kwargs={'slug':self.slug})

    def get_update_url(self):
        return reverse('organizer_tag:update', kwargs={'slug': self.slug})
    
    def get_delete_url(self):
        return reverse('organizer_tag:delete', kwargs={'slug': self.slug})


class Startup(models.Model):
    name = models.CharField(max_length=31, db_index=True)
    slug = models.SlugField(max_length=31, unique=True, help_text="A label for url config.")
    description = models.TextField()
    founded_date = models.DateField('date founded')
    contact = models.EmailField()
    website = models.URLField(max_length=255)
    tags = models.ManyToManyField(Tag, related_name='startups', blank=True)

    class Meta:
        ordering = ['name']
        get_latest_by = 'founded_date'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('organizer_startup:detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('organizer_startup:update', kwargs={'slug': self.slug})
    
    def get_delete_url(self):
        return reverse('organizer_startup:delete', kwargs={'slug':self.slug})
    


class Newslink(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=63)
    pub_date = models.DateField('date published')
    link = models.URLField(max_length=255)
    startup = models.ForeignKey(Startup)

    class Meta:
        verbose_name = 'news article'
        ordering = ['-pub_date']
        get_latest_by = 'pub_date'
        unique_together = ('slug','startup')

    def __str__(self):
        return "{}:{}".format(self.startup, self.title)
    
    def get_absolute_url(self):
        return self.startup.get_absolute_url()

    def get_update_url(self):
        return reverse('organizer_newslink:update', kwargs={'pk':self.pk})
    
    def get_delete_url(self):
        return reverse('organizer_newslink:delete', kwargs={'pk':self.pk})
    
    
