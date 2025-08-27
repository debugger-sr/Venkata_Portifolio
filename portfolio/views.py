from django.shortcuts import render
from .models import Skill, Experience, Project, Certification, Testimonial

# Create your views here.
def portfolio_view(request):
    # Fetch all objects from the database
    skills = Skill.objects.all()
    experiences = Experience.objects.order_by('-start_date') # Order by most recent job
    projects = Project.objects.all()
    certifications = Certification.objects.all()
    testimonials = Testimonial.objects.all()

    # Create a context dictionary to pass the data to the template
    context = {
        'skills': skills,
        'experiences': experiences,
        'projects': projects,
        'certifications': certifications,
        'testimonials': testimonials,
    }
    
    # Render the template with the context data
    return render(request, 'portfolio/index.html', context)