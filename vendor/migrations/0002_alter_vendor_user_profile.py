# Generated by Django 4.0.6 on 2022-08-01 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_userprofile_created_at'),
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='user_profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofilem', to='accounts.userprofile'),
        ),
    ]
