# Generated by Django 3.0.6 on 2020-06-06 10:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='部活名')),
                ('created_as', models.TimeField(default=datetime.datetime(2020, 6, 6, 10, 34, 3, 656415, tzinfo=utc), verbose_name='日付')),
            ],
        ),
        migrations.AlterField(
            model_name='department',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 6, 10, 34, 3, 615416, tzinfo=utc), verbose_name='日付'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 6, 10, 34, 3, 657414, tzinfo=utc), verbose_name='日付'),
        ),
        migrations.AddField(
            model_name='employee',
            name='club',
            field=models.ManyToManyField(to='employee.Club', verbose_name='部活'),
        ),
    ]
