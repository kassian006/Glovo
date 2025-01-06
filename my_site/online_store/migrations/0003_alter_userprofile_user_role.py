# Generated by Django 5.1.4 on 2025-01-04 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0002_userprofile_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_role',
            field=models.CharField(choices=[('client', 'Client'), ('courier', 'Courier'), ('owner', 'Owner')], default='client', max_length=16),
        ),
    ]
