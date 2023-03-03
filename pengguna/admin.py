from django.contrib import admin
from .models import Profile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('nama','no_kad_pengenalan','jantina','kelas','telefon')

    def no_kad_pengenalan(self, obj):
        return obj.nokp

admin.site.register(Profile, ProfileAdmin)

admin.site.site_header="AbuZahrah 2023 Administration"
