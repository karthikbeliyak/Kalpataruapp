# Generated by Django 2.2.7 on 2019-12-08 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalpataruapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plant',
            options={},
        ),
        migrations.AlterField(
            model_name='plant',
            name='category',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='plant',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
        migrations.AlterIndexTogether(
            name='plant',
            index_together=set(),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='slug',
        ),
    ]
