from django.db import migrations, models
from django.contrib.auth.models import AbstractUser


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('password', models.CharField(max_length=128)),
                ('first_name', models.CharField(max_length=150, blank=True)),
                ('last_name', models.CharField(max_length=150, blank=True)),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
