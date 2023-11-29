from django.contrib import admin

from hotel.models import HeroSection, About, Testimony, MasterRoom, Menu, Blogs, InstagramImage, Room, Booking

# Register your models here.
admin.site.register(HeroSection)
admin.site.register(About)
admin.site.register(Testimony)
admin.site.register(MasterRoom)
admin.site.register(Menu)
admin.site.register(Blogs)
admin.site.register(InstagramImage)
# admin.site.register(Book)
admin.site.register(Room)
admin.site.register(Booking)
