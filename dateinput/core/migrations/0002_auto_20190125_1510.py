# Generated by Django 2.1.5 on 2019-01-25 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entity',
            name='date',
        ),
        migrations.AddField(
            model_name='entity',
            name='date_type_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='entity',
            name='date_type_text',
            field=models.DateField(null=True),
        ),
    ]
