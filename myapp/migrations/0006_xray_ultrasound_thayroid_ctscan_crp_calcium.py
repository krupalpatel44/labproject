# Generated by Django 4.0 on 2024-09-14 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_blood_urine_remove_btest2_report_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='xray',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.BigIntegerField()),
                ('testname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.ourservices')),
            ],
        ),
        migrations.CreateModel(
            name='ultrasound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.BigIntegerField()),
                ('testname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.ourservices')),
            ],
        ),
        migrations.CreateModel(
            name='Thayroid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.BigIntegerField()),
                ('testname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.ourservices')),
            ],
        ),
        migrations.CreateModel(
            name='ctscan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.BigIntegerField()),
                ('testname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.ourservices')),
            ],
        ),
        migrations.CreateModel(
            name='CRP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.BigIntegerField()),
                ('testname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.ourservices')),
            ],
        ),
        migrations.CreateModel(
            name='Calcium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.BigIntegerField()),
                ('testname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.ourservices')),
            ],
        ),
    ]
