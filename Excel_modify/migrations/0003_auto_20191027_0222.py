# Generated by Django 2.2.1 on 2019-10-26 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Excel_modify', '0002_auto_20191026_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excel_details',
            name='excel_record',
            field=models.FileField(upload_to='excel_files'),
        ),
    ]
