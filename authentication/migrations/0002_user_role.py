# Generated by Django 4.2.6 on 2023-11-08 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('hr', 'hr'), ('employee', 'employee'), ('unknown', 'unknown')], default='unknown', max_length=8),
        ),
    ]
