# Generated by Django 3.2.13 on 2022-07-09 08:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import djstripe.enums
import djstripe.fields


class Migration(migrations.Migration):

    dependencies = [
        ("djstripe", "0016_alter_payout_destination"),
    ]

    operations = [
        migrations.CreateModel(
            name="InvoiceOrLineItem",
            fields=[
                (
                    "id",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                (
                    "type",
                    djstripe.fields.StripeEnumField(
                        enum=djstripe.enums.InvoiceorLineItemType, max_length=12
                    ),
                ),
            ],
        ),
    ]
