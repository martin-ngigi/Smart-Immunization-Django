# Generated by Django 4.1.2 on 2022-11-22 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts2', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userimmunization',
            options={'ordering': ('immunizationName',)},
        ),
    ]