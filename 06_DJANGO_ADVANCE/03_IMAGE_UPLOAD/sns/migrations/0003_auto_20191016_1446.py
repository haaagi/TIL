# Generated by Django 2.2.6 on 2019-10-16 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0002_auto_20191016_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='posting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='sns.Posting'),
        ),
    ]