from django.db import models

class Blog(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=255)
    body = models.TextField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def short_summary(self):
        return f"{self.body[:100]}..."
    
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
