# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'mytodo_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project_title', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'mytodo', ['Project'])

        # Adding model 'Task'
        db.create_table(u'mytodo_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task_title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('task_createdAt', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('task_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('task_priority', self.gf('django.db.models.fields.IntegerField')(default=2, max_length=1, blank=True)),
            ('task_dueDate', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('task_estimated', self.gf('django.db.models.fields.IntegerField')()),
            ('task_list', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mytodo.Project'])),
            ('task_pomodori', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('task_completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'mytodo', ['Task'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'mytodo_project')

        # Deleting model 'Task'
        db.delete_table(u'mytodo_task')


    models = {
        u'mytodo.project': {
            'Meta': {'object_name': 'Project'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project_title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'mytodo.task': {
            'Meta': {'object_name': 'Task'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task_completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'task_createdAt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'task_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'task_dueDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'task_estimated': ('django.db.models.fields.IntegerField', [], {}),
            'task_list': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mytodo.Project']"}),
            'task_pomodori': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'task_priority': ('django.db.models.fields.IntegerField', [], {'default': '2', 'max_length': '1', 'blank': 'True'}),
            'task_title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['mytodo']