# Generated by Django 4.0.4 on 2023-01-02 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_cuser_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuser',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='static/client/', width_field='width_field'),
        ),
    ]
