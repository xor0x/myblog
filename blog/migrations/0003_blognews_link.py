# Generated by Django 2.0.7 on 2018-07-28 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_sitesettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='blognews',
            name='link',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
