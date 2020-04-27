from django.contrib import admin
from .models import Post, Comment, Report
# Register your models here.




admin.site.register(Post)
admin.site.register(Comment)

#filtering for reports and displaying reports info on admin
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['post', 'report_reason', 'report']
    list_filter = ['post', 'report']
