#!/usr/local/bin/python

import yagmail

from random import shuffle
from array import array
from copy import deepcopy
#import smtplib

class Gmail(object):
    def __init__(self, email, password):

        self.email = email
        self.password = password
        #self.server = 'smtp.gmail.com'
        self.port = 587

        yagmail.register(email, password)
        self.session = yagmail.SMTP()

        #session = smtplib.SMTP_SSL(self.server, self.port)
        #session.ehlo()
        #session.starttls()
        #session.ehlo()
        #session.login(self.email, self.password)
        #self.session = session

    def send_message(self, to, subject, body):
        #''' This must be removed '''
        #headers = [
        #    "From: " + self.email,
        #    "Subject: " + subject,
        #    "To: " + to,
        #    "MIME-Version: 1.0",
        #"Content-Type: text/html"]
        #headers = "\r\n".join(headers)
        #self.session.sendmail(
        #    self.email,
        #    to,
        #    headers + "\r\n\r\n" + body)
        self.session.send(to, subject, body)

gm = Gmail('@gmail.com', '')

# emails = [
#     'shonnigford@gmail.com',
#     'shonnigford@gmail.com',
#     'shonnigford@gmail.com',
#     'TLease@Danscomp.com',
#     'curtisl@wdsra.com'
# ]
#
# names = [
#     {'name':'Seth','group':0},
#     {'name':'Evan','group':1},
#     {'name':'Rachel','group':2},
#     {'name':'Janel','group':3},
#     {'name':'Morgan','group':4},
#     {'name':'Ryan','group':4}
# ]

emails = [
    'shonnigford@gmail.com',
    'Todd.Honnigford@navistar.com',
    'jillmariecleveland@gmail.com',
    'annloochtan@gmail.com',
    'honnigford4@aol.com'
]

names = [
    {'name':'Scott','group':0},
    {'name':'Christine','group':0},
    {'name':'Seth','group':0},
    {'name':'Evan','group':0},
    {'name':'Todd','group':1},
    {'name':'Theresa','group':1},
    {'name':'Holly','group':1},
    {'name':'Jill','group':2},
    {'name':'Jason','group':2},
    {'name':'Ann','group':3},
    {'name':'Mike','group':3},
    {'name':'Mom','group':4},
    {'name':'Grandma','group':4}
]

attempt = 0

retry = True

givers = []

while retry:
    retry = False
    attempt = attempt + 1
    print "try # " + str(attempt)
    givers = deepcopy(names)
    receivers = deepcopy(names)
    shuffle(receivers)

    for g in givers:
        for r in receivers:
            if g['group'] != r['group'] and r['group'] != -1:
                g['give_to'] = r['name']
                r['group'] = -1
                break

        if 'give_to' not in g:
            print "none left!"
            retry = True
            break

count = 0
for e in emails:
    body = ""
    for g in givers:
        if g['group'] == count:
            body = body + g['name'] + " should buy for " + g['give_to'] + ".\n\n\n"
    gm.send_message(e, 'Christmas gifts', body)
    print e + ":  " + body
    count = count + 1
