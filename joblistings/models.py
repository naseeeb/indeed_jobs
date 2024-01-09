from djongo import models

class Job(models.Model):
    id = models.AutoField(primary_key=True)
    jobtitle = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    postdate = models.CharField(max_length=100)
    extractdate = models.DateField()
    summary = models.TextField()
    salary = models.CharField(max_length=50)
    job_url = models.URLField()

    def __str__(self):
        return self.jobtitle
