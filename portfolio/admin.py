from django.contrib import admin
from .models import Skill, Experience, Project, Certification, Testimonial

# Register your models here.
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(Certification)
admin.site.register(Testimonial)