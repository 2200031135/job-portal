# Generated by Django 4.2.4 on 2023-11-04 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_applyform_userlogin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyform',
            name='previous_experience',
            field=models.TextField(default='', null=True),
        ),
    ]
