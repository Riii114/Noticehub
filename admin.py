from django.contrib import admin
from myadmin.models import Notice

admin.site.site_header = 'Noticehub Web App'
admin.site.index_title = 'My Admin Panel'

# Register your models here.
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['id','subject','description','created_at','updated_at']

admin.site.register(Notice,NoticeAdmin)
