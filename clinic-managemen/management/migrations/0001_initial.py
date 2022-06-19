# Generated by Django 4.0.4 on 2022-05-20 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('image', models.ImageField(default='asset/profile-pic/default.png', upload_to='asset/profile-pic')),
                ('add_line_1', models.CharField(blank=True, max_length=50)),
                ('add_city', models.CharField(blank=True, max_length=50)),
                ('add_state', models.CharField(blank=True, max_length=20)),
                ('phone_no', models.IntegerField(blank=True, default=0)),
                ('add_Pincode', models.IntegerField(blank=True, default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('image', models.ImageField(default='asset/profile-pic/default.png', upload_to='asset/profile-pic')),
                ('qualification_higest', models.CharField(blank=True, max_length=40)),
                ('specilization', models.CharField(blank=True, max_length=100)),
                ('about', models.CharField(blank=True, max_length=500)),
                ('phone_no', models.IntegerField(blank=True, default=0)),
                ('add_line_1', models.CharField(blank=True, max_length=50)),
                ('add_city', models.CharField(blank=True, max_length=50)),
                ('add_state', models.CharField(blank=True, max_length=20)),
                ('add_Pincode', models.IntegerField(blank=True, default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Doctor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
