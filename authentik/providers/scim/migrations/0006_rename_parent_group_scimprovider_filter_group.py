# Generated by Django 4.1.7 on 2023-03-07 13:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("authentik_providers_scim", "0005_scimprovider_exclude_users_service_account_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="scimprovider",
            old_name="parent_group",
            new_name="filter_group",
        ),
    ]