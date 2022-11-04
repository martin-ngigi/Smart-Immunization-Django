# Generated by Django 4.1.2 on 2022-11-04 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('age', models.CharField(max_length=3)),
                ('nationId', models.CharField(max_length=8)),
                ('county', models.CharField(max_length=30)),
                ('registeredDate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('nationId',),
            },
        ),
        migrations.CreateModel(
            name='UserImmunization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('immunizationName', models.CharField(max_length=30)),
                ('immunizationDosageLevel', models.CharField(max_length=30)),
                ('immunizationDate', models.CharField(max_length=20)),
                ('nextImmunizationDate', models.CharField(max_length=30)),
                ('administeredDate', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='immunizations', to='accounts2.user')),
            ],
        ),
    ]
