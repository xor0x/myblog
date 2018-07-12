from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    pub_date = models.DateField()
    title_pro = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    text = models.TextField()

    class Meta:
        verbose_name_plural = "Projects"


    def __str__(self):
        return self.title

    def pub_date_b(self):
        return self.pub_date.strftime('%b %e %Y')
