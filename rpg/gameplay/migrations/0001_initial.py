# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Level'
        db.create_table(u'gameplay_level', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('level', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'gameplay', ['Level'])

        # Adding model 'Type'
        db.create_table(u'gameplay_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'gameplay', ['Type'])

        # Adding model 'Power'
        db.create_table(u'gameplay_power', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('power', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'gameplay', ['Power'])

        # Adding model 'Boss'
        db.create_table(u'gameplay_boss', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('age', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('difficulty', self.gf('django.db.models.fields.related.ForeignKey')(related_name='difficulty', to=orm['gameplay.Level'])),
        ))
        db.send_create_signal(u'gameplay', ['Boss'])

        # Adding model 'Trainer'
        db.create_table(u'gameplay_trainer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('age', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('accessory', self.gf('django.db.models.fields.TextField')()),
            ('level', self.gf('django.db.models.fields.related.ForeignKey')(related_name='levels', to=orm['gameplay.Level'])),
        ))
        db.send_create_signal(u'gameplay', ['Trainer'])

        # Adding model 'Pokemon'
        db.create_table(u'gameplay_pokemon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('health', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='types', to=orm['gameplay.Type'])),
            ('power', self.gf('django.db.models.fields.related.ForeignKey')(related_name='powers', to=orm['gameplay.Power'])),
        ))
        db.send_create_signal(u'gameplay', ['Pokemon'])


    def backwards(self, orm):
        # Deleting model 'Level'
        db.delete_table(u'gameplay_level')

        # Deleting model 'Type'
        db.delete_table(u'gameplay_type')

        # Deleting model 'Power'
        db.delete_table(u'gameplay_power')

        # Deleting model 'Boss'
        db.delete_table(u'gameplay_boss')

        # Deleting model 'Trainer'
        db.delete_table(u'gameplay_trainer')

        # Deleting model 'Pokemon'
        db.delete_table(u'gameplay_pokemon')


    models = {
        u'gameplay.boss': {
            'Meta': {'object_name': 'Boss'},
            'age': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'difficulty': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'difficulty'", 'to': u"orm['gameplay.Level']"}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'gameplay.level': {
            'Meta': {'object_name': 'Level'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'gameplay.pokemon': {
            'Meta': {'object_name': 'Pokemon'},
            'health': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'power': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'powers'", 'to': u"orm['gameplay.Power']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'types'", 'to': u"orm['gameplay.Type']"})
        },
        u'gameplay.power': {
            'Meta': {'object_name': 'Power'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'power': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'gameplay.trainer': {
            'Meta': {'object_name': 'Trainer'},
            'accessory': ('django.db.models.fields.TextField', [], {}),
            'age': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'levels'", 'to': u"orm['gameplay.Level']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'gameplay.type': {
            'Meta': {'object_name': 'Type'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['gameplay']