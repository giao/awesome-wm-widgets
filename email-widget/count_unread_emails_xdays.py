#!/usr/bin/python

import imaplib
import re
import datetime
import argparse

def login(user,password,conn):
    conn.login(user,password)
    conn.list
    readonly = True
    conn.select("INBOX", readonly)

dbg = False
def DBG(arg):
    if dbg is True :
        print(arg)

parser = argparse.ArgumentParser(description='Parsing arguments')
parser.add_argument('opt_pos_arg', type=int, nargs='?', help='Optional number of days')
args = parser.parse_args()
numdays = 0 if args.opt_pos_arg is None else args.opt_pos_arg

CONN = imaplib.IMAP4_SSL("mail",993)
login("giao", "lsdthc25", CONN)
date = (datetime.date.today() - datetime.timedelta(numdays)).strftime("%d-%b-%Y")
# #(_, data) = CONN.search(None, ('UNSEEN'), '(SENTSINCE {0})'.format(date), '(FROM {0})'.format("someone@yahoo.com".strip()))
(_, data) = CONN.search(None, ('UNSEEN'), '(SENTSINCE {0})'.format(date))
ids = data[0].split()

DBG(CONN.status("INBOX","(MESSAGES UNSEEN)"))
print(len(ids))

