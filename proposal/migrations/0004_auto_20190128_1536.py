# Generated by Django 2.0 on 2019-01-28 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposal', '0003_proposal_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='date_added',
            field=models.DateTimeField(auto_now=True),
        ),
    ]