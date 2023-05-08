# Generated by Django 4.2 on 2023-05-02 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RealEstate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('bedrooms', models.CharField(max_length=255)),
                ('bathrooms', models.CharField(max_length=255)),
                ('agent_name', models.CharField(max_length=255)),
                ('aria_code', models.CharField(max_length=255)),
                ('telephones', models.CharField(max_length=255)),
                ('prices', models.CharField(max_length=255)),
                ('highrespath', models.CharField(max_length=1000)),
                ('medrespath', models.CharField(max_length=1000)),
                ('lowrespath', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'real_estate',
            },
        ),
    ]