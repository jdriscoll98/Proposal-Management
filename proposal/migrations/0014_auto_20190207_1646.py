# Generated by Django 2.0 on 2019-02-07 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proposal', '0013_auto_20190201_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposal',
            name='num_of_downvotes',
        ),
        migrations.RemoveField(
            model_name='proposal',
            name='num_of_upvotes',
        ),
    ]
