from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50,
            choices=[
                ('cleaning', 'Home Cleaning'),
                ('plumping', 'Plumbing'),
                ('electrician','Electrician'),
                ('carpentry', 'Carpentry'),
                ('painting', 'Painting')
            ])
    price = models.DecimalField(max_digits=10, decimal_places=2)



    def __str__(self):
        return f"Service : {self.name}"