import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PartitionConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_label', models.TextField(unique=True)),
                ('period', models.TextField(default='Month')),
                ('interval', models.PositiveIntegerField(null=True)),
                ('attach_tablespace', models.TextField(null=True)),
                ('detach_tablespace', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PartitionLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_name', models.TextField(unique=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('is_attached', models.BooleanField(default=True)),
                ('detach_time', models.DateTimeField(null=True)),
                ('config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='pg_timepart.PartitionConfig')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
