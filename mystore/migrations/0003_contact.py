# Generated by Django 2.1.4 on 2018-12-16 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0002_m_khach_hang'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ho_ten', models.CharField(max_length=264)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('noi_dung', models.TextField()),
            ],
            options={
                'db_table': 'Contact',
            },
        ),
    ]
