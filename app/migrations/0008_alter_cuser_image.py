# Generated by Django 4.0.4 on 2023-01-02 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_cuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/client/'),
        ),
    ]
