# Generated by Django 4.2.5 on 2023-10-03 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobpostings', '0002_rename_company_jobposting_company_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobposting',
            old_name='company_id',
            new_name='company',
        ),
    ]
