from django.db import models
from django.db.models import Avg
from django.urls import reverse
from imagekit.models import ImageSpecField 
from imagekit.processors import ResizeToFill
from .fields import OrderField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True,
                            null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('shop:product_list_by_category',
                           args=[self.slug])




class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, null=True)
    image = models.ImageField(upload_to='product_images/',
                              blank=True)
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(90,90)], format='PNG', options={'quality': 60})
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def average_rating(self):
        return self.review_set.aggregate(Avg('rating'))['rating__avg']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('shop:product_detail',
                           args=[self.id, self.slug])

class ProductDetailImages(models.Model):

    def upload_path(self, filename):
        if "hat" in filename:
            return 'product_images/loopHat/' + "%s" %( filename)
        elif "beanie" in filename:
            return 'product_images/loopBeanie/' + "%s" %( filename)
        elif "croptop" in filename:
            return 'product_images/loopCropTop/' + "%s" %( filename)
        elif "hoodie" in filename:
            return 'product_images/loopHoodies/' + "%s" %( filename)
        elif "tshirt" in filename:
            return 'product_images/loopShirt/' + "%s" %( filename)
        elif "longsleeve" in filename:
            return 'product_images/loopLongsleeve/' + "%s" %( filename)
        elif "socks" in filename:
            return 'product_images/loopSocks/' + "%s" %( filename)
        elif "ff" in filename:
            return 'product_images/loopFlipFlops/' + "%s" %( filename)
        elif "i7" in filename:
            return 'product_images/loopIphoneCover/' + "%s" %( filename)
        elif "SG" in filename:
            return 'product_images/loopPhoneCovers/' + "%s" %( filename)
        elif "bag" in filename:
            return 'product_images/loopBag/' + "%s" %( filename)
        else:
            return 'product_images/'

    product = models.ForeignKey(Product, default=None, 
                                related_name='detail_images',
                                on_delete=models.CASCADE)
    detail_image = models.ImageField(upload_to=upload_path,
                                    blank=True)    
    image_thumbnail = ImageSpecField(source='detail_image', processors=[ResizeToFill(90,90)], format='PNG', options={'quality': 60})


class Review(models.Model):
    RATING_CHOICES = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
    ) 
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length = 200)
    rating = models.IntegerField(choices=RATING_CHOICES)
    order = OrderField(blank=True, for_fields=['product']) 
    product = models.CharField(max_length = 250, null= True)
    
    class Meta:
        ordering = ['order']  

