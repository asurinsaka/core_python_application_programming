#!/usr/bin/env python

from atexit import register
from re import compile
from threading import Thread
from time import ctime
#from urllib.request import urlopen as uopen
import urllib.request as urllib2

REGEX = compile('#([\d,]+) in Books')
AMZN = 'http://amazon.com/dp/'
ISBNs = {
    '0132269937': 'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals',
}

def getRanking(isbn):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    page = opener.open('%s%s' % (AMZN, isbn))
    data = page.read()
    page.close()
    #print(data)
    return REGEX.findall(data.decode("utf-8"))[0]

def _showRanking(isbn):
    print('- %r ranked %s' % (
        ISBNs[isbn], getRanking(isbn)
    ))

def _main():
    print('At', ctime(), 'on Amazone...')
    for isbn in ISBNs:
        Thread(target=_showRanking, args=(isbn,)).start()

@register
def _atexit():
    print('all DONE at:', ctime())

if __name__ == '__main__':
    _main()