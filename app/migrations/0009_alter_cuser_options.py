# Generated by Django 4.0.4 on 2023-01-02 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_cuser_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cuser',
            options={'verbose_name': 'Cuser', 'verbose_name_plural': 'Cusers'},
        ),
    ]
