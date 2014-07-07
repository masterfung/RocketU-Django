# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Genre'
        db.create_table(u'hollywood_genre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'hollywood', ['Genre'])

        # Adding model 'Video'
        db.create_table(u'hollywood_video', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('video', self.gf('embed_video.fields.EmbedVideoField')(max_length=200)),
        ))
        db.send_create_signal(u'hollywood', ['Video'])

        # Adding model 'Movie'
        db.create_table(u'hollywood_movie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('release_year', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('length', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('imdb', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('genre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hollywood.Genre'])),
            ('video', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hollywood.Video'])),
        ))
        db.send_create_signal(u'hollywood', ['Movie'])

        # Adding model 'Actor'
        db.create_table(u'hollywood_actor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('age', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'hollywood', ['Actor'])

        # Adding M2M table for field movies on 'Actor'
        m2m_table_name = db.shorten_name(u'hollywood_actor_movies')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('actor', models.ForeignKey(orm[u'hollywood.actor'], null=False)),
            ('movie', models.ForeignKey(orm[u'hollywood.movie'], null=False))
        ))
        db.create_unique(m2m_table_name, ['actor_id', 'movie_id'])


    def backwards(self, orm):
        # Deleting model 'Genre'
        db.delete_table(u'hollywood_genre')

        # Deleting model 'Video'
        db.delete_table(u'hollywood_video')

        # Deleting model 'Movie'
        db.delete_table(u'hollywood_movie')

        # Deleting model 'Actor'
        db.delete_table(u'hollywood_actor')

        # Removing M2M table for field movies on 'Actor'
        db.delete_table(db.shorten_name(u'hollywood_actor_movies'))


    models = {
        u'hollywood.actor': {
            'Meta': {'object_name': 'Actor'},
            'age': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movies': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['hollywood.Movie']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hollywood.genre': {
            'Meta': {'object_name': 'Genre'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hollywood.movie': {
            'Meta': {'object_name': 'Movie'},
            'genre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hollywood.Genre']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imdb': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'length': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'release_year': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hollywood.Video']"})
        },
        u'hollywood.video': {
            'Meta': {'object_name': 'Video'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'video': ('embed_video.fields.EmbedVideoField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['hollywood']