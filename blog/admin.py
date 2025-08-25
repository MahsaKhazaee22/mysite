from django.contrib import admin
from blog.models import Post,Category


# Register your models here.

# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    # fields = ('title',) just shoe title
    list_display = ('title','author','counted_views','published_date','created_date','status')
    list_filter = ('status','author',)
    # ordering = ['-created_date']
    search_fields = ['title','content']

admin.site.register(Category)    
admin.site.register(Post,PostAdmin)