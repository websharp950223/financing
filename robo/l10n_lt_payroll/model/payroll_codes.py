# -*- coding: utf-8 -*-

WATCH_HOME = [u'BN']
WATCH_WORK = [u'BĮ']
EXTRA = [u'DN', u'DP']
OVERTIME = [u'SNV', u'VD', u'VDN', u'VSS', u'VDS']
REGULAR = [u'FD', u'KS', u'NT', u'DLS']
SUMINE = [u'VDL', u'NDL']
OUT_OF_OFFICE = [u'KV', u'MD']
UNPAID_OUT_OF_OFFICE = [u'KVN']
OTHER_PAID = [u'ID', u'M', u'MP']
DOWNTIME = [u'PN', u'PK']
OTHER_SPECIAL = [u'V']

PAYROLL_CODES = {
    'WATCH_HOME': WATCH_HOME,
    'WATCH_WORK': WATCH_WORK,
    'BUDEJIMAS': WATCH_HOME + WATCH_WORK,
    'EXTRA': EXTRA,
    'OVERTIME': OVERTIME,
    'ALL_EXTRA': EXTRA + OVERTIME,
    'REGULAR': REGULAR,
    'SUMINE': SUMINE,
    'OUT_OF_OFFICE': OUT_OF_OFFICE,
    'UNPAID_OUT_OF_OFFICE': UNPAID_OUT_OF_OFFICE,
    'OTHER_PAID': OTHER_PAID,
    'OTHER_SPECIAL': OTHER_SPECIAL,
    'NORMAL': WATCH_HOME + WATCH_WORK + EXTRA + OVERTIME + REGULAR + OTHER_PAID,
    'WORKED': WATCH_HOME + WATCH_WORK + EXTRA + OVERTIME + REGULAR,
    'DOWNTIME': DOWNTIME,
}
