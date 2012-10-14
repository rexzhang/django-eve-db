#coding=utf-8


"""
Import translation data.
"""
from eve_db.models import *
from importer_classes import SQLImporter, parse_int_bool, parse_char_notnull


class Importer_trnTranslations(SQLImporter):
    model = TrnTranslations
    pks = (('tc', 'tcID'), ('key', 'keyID'), ('language', 'languageID', False)) #add False, because pks is't primary key
    field_map = (('text', 'text'),)
