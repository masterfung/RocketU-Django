# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Movie.poster'
        db.alter_column(u'tomatoes_movie', 'poster', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

    def backwards(self, orm):

        # Changing field 'Movie.poster'
        db.alter_column(u'tomatoes_movie', 'poster', self.gf('django.db.models.fields.URLField')(default=2, max_length=200))

    models = {
        u'tomatoes.movie': {
            'Meta': {'object_name': 'Movie'},
            'audience_score': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True'}),
            'critics_score': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mpaa_rating': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'poster': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'release_year': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'runtime': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['tomatoes']