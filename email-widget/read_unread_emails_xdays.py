#!/usr/bin/python

import imaplib
import email
import datetime

def process_mailbox(M):
    numdays=0
    date = (datetime.date.today() - datetime.timedelta(numdays)).strftime("%d-%b-%Y")
    rv, data = M.search(None, "(UNSEEN)", '(SENTSINCE {0})'.format(date))
    if rv != 'OK':
        print "No messages found!"
        return

    for num in data[0].split():
        rv, data = M.fetch(num, '(BODY.PEEK[])')
        if rv != 'OK':
            print "ERROR getting message", num
            return

        msg = email.message_from_string(data[0][1])
        print 'From:', msg['From']
        subject = msg if len(msg['Subject']) < 43 else msg['Subject'][:40]+'...'
        #print 'Subject: %s' % (msg['Subject'][:32])
        print '   Subject: %s' % (subject)
        date_tuple = email.utils.parsedate_tz(msg['Date'])
        if date_tuple:
            local_date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
            print "   Date:", local_date.strftime("%a, %d %b %Y %H:%M:%S")
            # with code below you can process text of email
            # if msg.is_multipart():
            #     for payload in msg.get_payload():
            #         if payload.get_content_maintype() == 'text':
            #             print  payload.get_payload()
            #         else:
            #             print msg.get_payload()


##M=imaplib.IMAP4_SSL("mail.teenagemutantninjaturtles.com", 993)
##M.login("mickey@tmnt.com","cowabunga")
M=imaplib.IMAP4_SSL("mail", 993)
M.login("giao","lsdthc25")

rv, data = M.select("INBOX")
if rv == 'OK':
    process_mailbox(M)
M.close()
M.logout()
