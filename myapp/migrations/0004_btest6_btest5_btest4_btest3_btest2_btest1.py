# Generated by Django 4.0 on 2024-09-14 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_ourservices'),
    ]

    operations = [
        migrations.CreateModel(
            name='btest6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.BigIntegerField()),
                ('test', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.ourservices')),
            ],
        ),
        migrations.CreateModel(
            name='btest5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.BigIntegerField()),
                ('test', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.ourservices')),
            ],
        ),
        migrations.CreateModel(
            name='btest4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.BigIntegerField()),
                ('test', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.ourservices')),
            ],
        ),
        migrations.CreateModel(
            name='btest3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.BigIntegerField()),
                ('test', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.ourservices')),
            ],
        ),
        migrations.CreateModel(
            name='btest2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.BigIntegerField()),
                ('test', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.ourservices')),
            ],
        ),
        migrations.CreateModel(
            name='btest1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.BigIntegerField()),
                ('test', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.ourservices')),
            ],
        ),
    ]
