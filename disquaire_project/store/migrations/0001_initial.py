# Generated by Django 3.2.9 on 2021-11-17 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('available', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=200)),
                ('picture', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('contacted', models.BooleanField(default=False)),
                ('album', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.album')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.contact')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artists',
            field=models.ManyToManyField(blank=True, related_name='albums', to='store.Artist'),
        ),
    ]
