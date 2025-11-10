from django.contrib import admin
from .models.models import Office
from .models.employee import Employee
from .models.leaders import Leader
from django.utils.html import format_html
from .models.notice import Notice

# Register the model
admin.site.register(Office)
admin.site.register(Employee)

# admin.site.register(Leader)
@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    list_display = ('leader_name', 'leader_position', 'leader_contact', 'leader_email', 'leader_photo_thumbnail')
    search_fields = ('leader_name', 'leader_position', 'leader_email')
    list_filter = ('leader_position',)

    def leader_photo_thumbnail(self, obj):
        if obj.leader_photo:
            return format_html('<img src="{}" style="height:50px;width:50px;border-radius:50%;" />', obj.leader_photo.url)
        return "-"
    leader_photo_thumbnail.short_description = 'Photo'
@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('notice_title','notice_published_date')
    search_fields= ('notice_title','notice_published_date')
    list_filter = ('notice_title','notice_published_date')