# Generated by Django 5.0.3 on 2024-03-30 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QRQC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_date', models.DateField()),
                ('opening_department', models.CharField(max_length=100)),
                ('responsible_department', models.CharField(max_length=100)),
                ('customer_complaint', models.TextField()),
                ('product_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('responsible_person', models.CharField(max_length=100)),
                ('next_report_date', models.DateField()),
                ('preventive_action', models.TextField()),
                ('root_cause', models.TextField()),
                ('taken_action', models.TextField()),
                ('error_proofing_identification', models.BooleanField()),
                ('lpa_update', models.BooleanField()),
                ('accepted_action', models.BooleanField()),
                ('pcp_pfmea_update', models.BooleanField()),
                ('standardized_work_instruction_update', models.BooleanField()),
                ('conclusions', models.TextField()),
                ('action_item', models.TextField()),
                ('estimated_closure_date', models.DateField()),
                ('actual_closure_date', models.DateField()),
                ('customer_closure_date', models.DateField()),
                ('general_status', models.CharField(choices=[('Red', 'Red'), ('Green', 'Green'), ('Yellow', 'Yellow'), ('N/A', 'N/A')], max_length=10)),
            ],
        ),
    ]