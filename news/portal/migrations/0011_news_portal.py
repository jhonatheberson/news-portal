# Generated by Django 3.0.2 on 2020-01-16 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0010_portal'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='portal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.Portal'),
        ),
    ]