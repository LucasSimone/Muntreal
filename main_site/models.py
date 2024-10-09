from django.db import models
from django.utils import timezone
from django.utils.html import mark_safe
from django.conf import settings

    
# # Example of a Model creation with different options
# class ExampleModel(models.Model):
#     # Below is a char field with set choices
#     priority_level = [
#         ("HI", "High"),
#         ("MD", "Medium"),
#         ("LW", "Low"),
#         ("NN", "None"),
#     ]

#     priority = models.CharField(
#         max_length=2,
#         choices=priority_level,
#         default="NN"
#     )

#     # Sets a custom table name
#     class Meta:
#         verbose_name_plural = "Name"

class Person(models.Model):
    name = models.CharField(blank=True, default=None,max_length=255)

    class Meta:
        verbose_name_plural = "People"

    def __str__(self):
        return self.name

def my_func():
    print("YEs")

class Image(models.Model):

    image = models.ImageField(upload_to='images',default=my_func)
    date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(blank=True, null=True, default=None, max_length=255)
    people = models.ManyToManyField(Person,related_name='model',blank=True,)
    photographer = models.ManyToManyField(Person,related_name='photographer',blank=True,)
    camera = models.CharField(blank=True, null=True, default=None, max_length=255)


    # Sets a custom table name
    class Meta:
        verbose_name_plural = "Images"

    def image_tag(self):
            return mark_safe('<img src="%s" style="max-width:350px;max-height: 250px;" />' % (settings.MEDIA_URL + str(self.image)))
    
    image_tag.short_description = 'Image Preview'


class Feedback(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    date_recieved = models.DateTimeField(default=timezone.now)
    ip_address = models.GenericIPAddressField(null=True,blank=True)
    content = models.TextField()

    priority_level = [
        (0, "New"),
        (1, "High"),
        (2, "Medium"),
        (3, "Low"),
        (4, "None"),
    ]

    priority = models.IntegerField(choices=priority_level,default=0)

    class Meta:
        verbose_name_plural = "Feedback"

class Testimonial(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128,null=True,blank=True)
    content = models.TextField()
    date_recieved = models.DateTimeField(default=timezone.now,null=True,blank=True)
