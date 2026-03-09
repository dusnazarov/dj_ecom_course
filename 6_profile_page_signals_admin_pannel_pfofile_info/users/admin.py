from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User


admin.site.register(Profile)


# Mix the Profile model into the User Admin
class ProfileInline(admin.StackedInline):
    model = Profile

# Extend the User Admin to include the Profile
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    inlines = [ProfileInline]

# Unregister the default User admin and register the new one
admin.site.unregister(User)

# Register the new User admin
admin.site.register(User, UserAdmin)
 