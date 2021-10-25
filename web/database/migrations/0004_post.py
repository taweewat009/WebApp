# Generated by Django 3.2.8 on 2021-10-25 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_alter_guestbook_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('author', models.TextField()),
                ('category', models.TextField()),
            ],
        ),
    ]