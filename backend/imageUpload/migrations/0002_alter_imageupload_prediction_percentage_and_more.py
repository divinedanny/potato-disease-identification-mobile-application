# Generated by Django 4.1.3 on 2023-01-11 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("imageUpload", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="imageupload",
            name="prediction_percentage",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="imageupload",
            name="prediction_text",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
