# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Player.real_name'
        db.alter_column(u'superhero_player', 'real_name', self.gf('django.db.models.fields.CharField')(max_length=120))

    def backwards(self, orm):

        # Changing field 'Player.real_name'
        db.alter_column(u'superhero_player', 'real_name', self.gf('django.db.models.fields.TextField')())

    models = {
        u'superhero.location': {
            'Meta': {'object_name': 'Location'},
            'fighting_location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tournament': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'teams'", 'symmetrical': 'False', 'to': u"orm['superhero.Team']"})
        },
        u'superhero.player': {
            'Meta': {'object_name': 'Player'},
            'age': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'real_name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'superhero_name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'superhero.power': {
            'Meta': {'object_name': 'Power'},
            'good_bad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'powers'", 'to': u"orm['superhero.Player']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'power': ('django.db.models.fields.TextField', [], {})
        },
        u'superhero.team': {
            'Meta': {'object_name': 'Team'},
            'alliance': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'affiliations'", 'to': u"orm['superhero.Player']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['superhero']