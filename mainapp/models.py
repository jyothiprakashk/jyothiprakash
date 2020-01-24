from django.db import models
from datetime import datetime 
class Portfolio(models.Model):
    title=models.CharField(max_length=30,verbose_name="title")
    data=models.TextField()
    live_demo=models.URLField()
    source_code=models.URLField()
    tools=models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
        