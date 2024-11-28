from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Creator(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    categories = models.ManyToManyField(Category, through='CreatorCategory' ,related_name='creators')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CreatorCategory(models.Model):
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('creator', 'category')
    def __str__(self):
        return f"{self.creator.name} - { self.category.name}"


class Channel(models.Model):
    PLATFORM_CHOICES = [
        ('Youtube', "Youtube"),
        ('Instagram', 'Instagram'),
        ('X', 'X'),
        ('Other', 'Other'),
    ]

    creator = models.ForeignKey(
        Creator, related_name='channels', on_delete=models.CASCADE)
    platform = models.CharField(
        max_length=50, choices=PLATFORM_CHOICES, default='Other')
    url = models.URLField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.platform } - {self.creator.name}"
