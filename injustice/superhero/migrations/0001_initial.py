# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Player'
        db.create_table(u'superhero_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('superhero_name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('real_name', self.gf('django.db.models.fields.TextField')()),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('age', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
        ))
        db.send_create_signal(u'superhero', ['Player'])

        # Adding model 'Team'
        db.create_table(u'superhero_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('alliance', self.gf('django.db.models.fields.related.ForeignKey')(related_name='affiliations', to=orm['superhero.Player'])),
        ))
        db.send_create_signal(u'superhero', ['Team'])

        # Adding model 'Power'
        db.create_table(u'superhero_power', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('power', self.gf('django.db.models.fields.TextField')()),
            ('good_bad', self.gf('django.db.models.fields.related.ForeignKey')(related_name='powers', to=orm['superhero.Player'])),
        ))
        db.send_create_signal(u'superhero', ['Power'])

        # Adding model 'Location'
        db.create_table(u'superhero_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fighting_location', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'superhero', ['Location'])

        # Adding M2M table for field tournament on 'Location'
        m2m_table_name = db.shorten_name(u'superhero_location_tournament')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('location', models.ForeignKey(orm[u'superhero.location'], null=False)),
            ('team', models.ForeignKey(orm[u'superhero.team'], null=False))
        ))
        db.create_unique(m2m_table_name, ['location_id', 'team_id'])


    def backwards(self, orm):
        # Deleting model 'Player'
        db.delete_table(u'superhero_player')

        # Deleting model 'Team'
        db.delete_table(u'superhero_team')

        # Deleting model 'Power'
        db.delete_table(u'superhero_power')

        # Deleting model 'Location'
        db.delete_table(u'superhero_location')

        # Removing M2M table for field tournament on 'Location'
        db.delete_table(db.shorten_name(u'superhero_location_tournament'))


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
            'real_name': ('django.db.models.fields.TextField', [], {}),
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