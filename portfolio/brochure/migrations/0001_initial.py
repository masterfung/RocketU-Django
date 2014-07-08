# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Language'
        db.create_table(u'brochure_language', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal(u'brochure', ['Language'])

        # Adding model 'Link'
        db.create_table(u'brochure_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal(u'brochure', ['Link'])

        # Adding model 'Project'
        db.create_table(u'brochure_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(related_name='languages', to=orm['brochure.Language'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('link', self.gf('django.db.models.fields.related.ForeignKey')(related_name='links', to=orm['brochure.Link'])),
        ))
        db.send_create_signal(u'brochure', ['Project'])


    def backwards(self, orm):
        # Deleting model 'Language'
        db.delete_table(u'brochure_language')

        # Deleting model 'Link'
        db.delete_table(u'brochure_link')

        # Deleting model 'Project'
        db.delete_table(u'brochure_project')


    models = {
        u'brochure.language': {
            'Meta': {'object_name': 'Language'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'brochure.link': {
            'Meta': {'object_name': 'Link'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'brochure.project': {
            'Meta': {'object_name': 'Project'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'languages'", 'to': u"orm['brochure.Language']"}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'links'", 'to': u"orm['brochure.Link']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        }
    }

    complete_apps = ['brochure']