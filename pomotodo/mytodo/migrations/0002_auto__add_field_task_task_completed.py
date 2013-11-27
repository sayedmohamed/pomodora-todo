# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Task.task_completed'
        db.add_column(u'mytodo_task', 'task_completed',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Task.task_completed'
        db.delete_column(u'mytodo_task', 'task_completed')


    models = {
        u'mytodo.list': {
            'Meta': {'object_name': 'List'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'mytodo.task': {
            'Meta': {'object_name': 'Task'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task_completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'task_createdAt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'task_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'task_dueDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'task_estimated': ('django.db.models.fields.IntegerField', [], {}),
            'task_list': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mytodo.List']"}),
            'task_pomodori': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'task_priority': ('django.db.models.fields.IntegerField', [], {'default': '2', 'max_length': '1', 'blank': 'True'}),
            'task_title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['mytodo']