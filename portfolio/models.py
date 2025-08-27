from django.db import models

# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=[
        ('Languages & Databases', 'Languages & Databases'),
        ('Data Engineering', 'Data Engineering'),
        ('Analytics & BI', 'Analytics & BI'),
    ])

    def __str__(self):
        return self.name

class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    technologies = models.CharField(max_length=200) # e.g., "Kafka, Spark, Snowflake"

    def __str__(self):
        return self.title
    
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    technologies = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    # Add this new method
    def get_technologies_list(self):
        return [tech.strip() for tech in self.technologies.split(',')]

class Certification(models.Model):
    name = models.CharField(max_length=100)
    issuing_organization = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='cert_logos/')

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    quote = models.TextField()
    author_name = models.CharField(max_length=100)
    author_title = models.CharField(max_length=100)

    def __str__(self):
        return f"Testimonial from {self.author_name}"