# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'PaymentMethod.enabled'
        db.delete_column(u'buysafe_paymentmethod', 'enabled')

        # Adding field 'PaymentMethod.is_enabled'
        db.add_column(u'buysafe_paymentmethod', 'is_enabled',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'PaymentMethod.enabled'
        db.add_column(u'buysafe_paymentmethod', 'enabled',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'PaymentMethod.is_enabled'
        db.delete_column(u'buysafe_paymentmethod', 'is_enabled')


    models = {
        u'buysafe.paymentmethod': {
            'Meta': {'ordering': "['-is_enabled', 'payment_type', '-id']", 'object_name': 'PaymentMethod'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'payment_type': ('django.db.models.fields.IntegerField', [], {}),
            'store_id': ('django.db.models.fields.CharField', [], {'max_length': '11'})
        }
    }

    complete_apps = ['buysafe']