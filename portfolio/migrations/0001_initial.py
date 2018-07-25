# Generated by Django 2.0.7 on 2018-07-25 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('pub_date', models.DateField()),
                ('title_pro', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Projects',
            },
        ),
    ]
