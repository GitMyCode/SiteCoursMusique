# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Generique'
        db.create_table(u'core_generique', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_creation', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modification', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('texteAcceuil', self.gf('django.db.models.fields.TextField')()),
            ('texteAcceuil_fr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('texteAcceuil_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('texteContact', self.gf('django.db.models.fields.TextField')()),
            ('texteContact_fr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('texteContact_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Generique'])

        # Adding model 'Professeurs'
        db.create_table(u'core_professeurs', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_creation', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modification', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('prenom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('biographie', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'core', ['Professeurs'])

        # Adding model 'Cours'
        db.create_table(u'core_cours', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_creation', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modification', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('instruments', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('instruments_fr', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('instruments_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('prix', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'core', ['Cours'])

        # Adding M2M table for field professeurs on 'Cours'
        m2m_table_name = db.shorten_name(u'core_cours_professeurs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cours', models.ForeignKey(orm[u'core.cours'], null=False)),
            ('professeurs', models.ForeignKey(orm[u'core.professeurs'], null=False))
        ))
        db.create_unique(m2m_table_name, ['cours_id', 'professeurs_id'])

        # Adding model 'Gallerie'
        db.create_table(u'core_gallerie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_creation', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modification', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('photos', self.gf('django.db.models.fields.files.ImageField')(default='media/photos/none/no-img.jpg', max_length=100)),
        ))
        db.send_create_signal(u'core', ['Gallerie'])

        # Adding model 'Blog'
        db.create_table(u'core_blog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'core', ['Blog'])

        # Adding model 'Comment'
        db.create_table(u'core_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('blog', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Blog'])),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('comment', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'core', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Generique'
        db.delete_table(u'core_generique')

        # Deleting model 'Professeurs'
        db.delete_table(u'core_professeurs')

        # Deleting model 'Cours'
        db.delete_table(u'core_cours')

        # Removing M2M table for field professeurs on 'Cours'
        db.delete_table(db.shorten_name(u'core_cours_professeurs'))

        # Deleting model 'Gallerie'
        db.delete_table(u'core_gallerie')

        # Deleting model 'Blog'
        db.delete_table(u'core_blog')

        # Deleting model 'Comment'
        db.delete_table(u'core_comment')


    models = {
        u'core.blog': {
            'Meta': {'object_name': 'Blog'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'core.comment': {
            'Meta': {'object_name': 'Comment'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Blog']"}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.cours': {
            'Meta': {'object_name': 'Cours'},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date_creation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modification': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instruments': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'instruments_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'instruments_fr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'prix': ('django.db.models.fields.FloatField', [], {}),
            'professeurs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Professeurs']", 'symmetrical': 'False'})
        },
        u'core.gallerie': {
            'Meta': {'object_name': 'Gallerie'},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date_creation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modification': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photos': ('django.db.models.fields.files.ImageField', [], {'default': "'media/photos/none/no-img.jpg'", 'max_length': '100'})
        },
        u'core.generique': {
            'Meta': {'object_name': 'Generique'},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date_creation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modification': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'texteAcceuil': ('django.db.models.fields.TextField', [], {}),
            'texteAcceuil_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'texteAcceuil_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'texteContact': ('django.db.models.fields.TextField', [], {}),
            'texteContact_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'texteContact_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'core.professeurs': {
            'Meta': {'object_name': 'Professeurs'},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'biographie': ('django.db.models.fields.TextField', [], {}),
            'date_creation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modification': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['core']