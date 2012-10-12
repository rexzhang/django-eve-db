"""
Translation-related models.
"""
from django.db import models

from eve_db.eve_db_settings import *

class TrnTranslations(models.Model):
    """
    CCP Table: trnTranslations
    CCP Primary key: ("tcID" smallint(6), "keyID" int(11),"languageID" varchar(50))
    """
    tc_id = models.IntegerField()
    key_id = models.IntegerField()
    #language_id = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    text = models.TextField()

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Translations'
        verbose_name_plural = 'Translations'
        unique_together = ('tc_id', 'key_id', 'language')

    def __unicode__(self):
        #return self.text
        return '%d %d %s: ' % (self.tc_id, self.key_id, self.language, self.text)

    def __str__(self):
        return self.__unicode__()
