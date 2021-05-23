from django.contrib import admin
from . import models
from django_summernote.admin import SummernoteModelAdmin




#admin.site.register(PostAdmin)

#RoomImagesTabular
class RoomImagesTabular(admin.TabularInline):
    model = models.RoomImages

#RoomAdmin
class RoomAdmin(SummernoteModelAdmin,admin.ModelAdmin):
    list_display = ['name','price','loc']
    inlines = [RoomImagesTabular,]
    fieldsets = (
        (None, {
            'fields': ('name','price','descripe','loc')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('image','files', 'category'),
        }),
    )
    #fields = ('name','price','loc' )

    #exclude = ('image',)
    summernote_fields = ('descripe',)


# Register your models here.
admin.site.register(models.Room,RoomAdmin)
admin.site.register(models.RoomImages)
admin.site.register(models.Category )
admin.site.register(models.RoomReview)
admin.site.register(models.RoomBook)