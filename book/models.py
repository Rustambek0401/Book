from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    category_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)

        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name


class Author(BaseModel):
    full_name = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=299,null=True,blank=True)
    adress = models.CharField(max_length=199)
    email = models.EmailField()
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.full_name)

        super(Author, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name


class Book(BaseModel):
    class RatingChoices(models.IntegerChoices):
        ZERO = 0
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    book_name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    rating = models.IntegerField(choices=RatingChoices.choices, default=RatingChoices.ZERO.value, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    author = models.ManyToManyField(Author)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')



    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.book_name)

        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.book_name

