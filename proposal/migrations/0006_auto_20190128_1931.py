# Generated by Django 2.0 on 2019-01-29 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposal', '0005_remove_proposal_source'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposal',
            name='accepted',
        ),
        migrations.AddField(
            model_name='proposal',
            name='status',
            field=models.CharField(choices=[('accepted', 'accepted'), ('pending', 'pending'), ('denied', 'denied')], default='pending', max_length=100),
        ),
    ]
