#!/usr/bin/env python

from concurrent.futures import ThreadPoolExecutor
from atexit import register
from re import compile
from threading import Thread
from time import ctime
#from urllib.request import urlopen as uopen
import urllib.request as urllib2

REGEX = compile(b'#([\d,]+) in Books')
AMZN = 'http://amazon.com/dp/'
ISBNs = {
    '0132269937': 'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals',
}

def getRanking(isbn):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    with opener.open('%s%s' % (AMZN, isbn)) as page:
        return str(REGEX.findall(page.read())[0], 'utf-8')




def _main():
    print('At', ctime(), 'on Amazone...')
    with ThreadPoolExecutor(3) as executor:
        for isbn, ranking in zip(
                ISBNs, executor.map(getRanking, ISBNs)):
            print('- %r ranked %s ' % (ISBNs[isbn], ranking))
    print('all DONE at:', ctime())


if __name__ == '__main__':
    _main()