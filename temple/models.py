from django.db import models
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse
from jainism.utils import unique_slugify
from django.template.defaultfilters import slugify

STATES = (
    'Jammu and Kashmir', 'Himachal Pradesh', 'Uttarakhand', 'Punjab', 'Haryana', 'Delhi', 'Uttar Pradesh', 'Assam', 'Meghalaya', 'Manipur',\
    'Mizoram','Nagaland', 'Sikkim', 'Tripura', 'Arunachal Pradesh', 'West Bengal', 'Rajasthan', 'Gujarat', 'Maharashtra', 'Goa',\
    'Madhya Pradesh', 'Bihar', 'Jharkhand', 'Chhattisgarh', 'Orissa', 'Karnataka', 'Kerala', 'Tamil Nadu', 'Andhra Pradesh')

class Tags(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def get_Temple(self):
        return self.temple_set.all()

    def get_absolute_url(self):
        return reverse('temples_list', kwargs={'pk': self.id})

    def __unicode__(self):
        return self.name

class Address(models.Model):
    street = models.CharField(max_length=350, blank=True, default = '')
    city = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=40, choices=zip(sorted(STATES), sorted(STATES)))
    pincode = models.PositiveIntegerField(blank=True, null=True)
    country = models.CharField(max_length=120, default='India')

    def __unicode__(self):
        return unicode('%s %s %s' %(self.street, self.city, self.state))

class Temple(models.Model):
    title = models.CharField(max_length=100, unique=True)
    images = models.ImageField(max_length=100, upload_to="{{ MEDIA_URL }}", null=True, blank=True)
    slug = models.SlugField(max_length=255)
    location = models.ForeignKey(Address)
    location_url = models.URLField(blank=True)
    tags = models.ManyToManyField(Tags)
    estd = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    author = models.ForeignKey(User, related_name="temples")
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('temple_detail', kwargs={'pk': self.id})

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_str = '%s' %self.title
            unique_slugify(self, slug_str)
        super(Temple, self).save(*args, **kwargs)
