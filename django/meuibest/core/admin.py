from django.contrib import admin
from .models import Category, Channel, Creator

# Register your models here.

@admin.register(Creator)
class CreatorAdmin(admin.ModelAdmin):
  list_display=('name', 'created_at')
  search_fields=('name',)
  filter_horizontal=('categories',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name',)
  search_fields = ('name',)

@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
  list_display=('platform', 'creator', 'url')
  search_fields=('creator__name', 'platform', 'url')