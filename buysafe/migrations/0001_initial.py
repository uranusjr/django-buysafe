# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PaymentMethod'
        db.create_table(u'buysafe_paymentmethod', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('payment_type', self.gf('django.db.models.fields.IntegerField')()),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('store_id', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'buysafe', ['PaymentMethod'])


    def backwards(self, orm):
        # Deleting model 'PaymentMethod'
        db.delete_table(u'buysafe_paymentmethod')


    models = {
        u'buysafe.paymentmethod': {
            'Meta': {'object_name': 'PaymentMethod'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'payment_type': ('django.db.models.fields.IntegerField', [], {}),
            'store_id': ('django.db.models.fields.CharField', [], {'max_length': '11'})
        }
    }

    complete_apps = ['buysafe']