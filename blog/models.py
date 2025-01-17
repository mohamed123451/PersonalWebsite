from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    url = models.URLField(blank=True)

    # to return string  when call the class without any attributes or methods
    # ex: print(str(first_blog)) instead of print(firstblog.__str__())
    def __str__(self):
        return self.title