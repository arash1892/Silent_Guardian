# Generated by Django 3.0.4 on 2020-03-30 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0002_user_banner_clicked'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clicks_Duplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('click_id', models.IntegerField()),
                ('banner_id', models.IntegerField()),
                ('campaign_id', models.IntegerField()),
            ],
        ),
    ]
