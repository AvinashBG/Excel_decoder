from django.db import models

class Excel_details(models.Model):
    excel_record=models.FileField(upload_to='excel_files',blank=False)

    def __str__(self):
        return str(self.excel_record).split("/")[-1]

# Create your models here.
