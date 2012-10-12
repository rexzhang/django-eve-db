#coding=utf-8


"""
Import translation data.
"""
from eve_db.models import *
from importer_classes import SQLImporter, parse_int_bool, parse_char_notnull


class Importer_trnTranslations(SQLImporter):
    model = TrnTranslations
    #pks = (('tc', 'tcID'), ('key', 'keyID'), ('language', 'languageID'))
    pks = (('tc', 'tcID'), ('key', 'keyID'), ('language', 'languageID', False)) #添加一个 False 可以避免因为作为主键组成部分而强制添加 '_id' 后缀
    field_map = (('text', 'text'),)
