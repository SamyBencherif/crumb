#!/usr/bin/python

import curses
from curses import wrapper
import sys

code = open(sys.argv[1], 'r').read()

def getIndexCoord(i):

    i = i % len(code.split())

    y = 0
    x = 0
    j = 0
    while i:
        if i:
            i -= 1
            j += 1
            x += 1
        while code[j] in ' \n\t':
            x += 1
            if code[j] == '\n':
                x = 0
                y += 1
            j += 1
    return j,y,x

def main(scr):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    h,w = scr.getmaxyx()

    scr.bkgd(' ', curses.color_pair(1))

    k = ""
    i = 0

    #scr.nodelay(True)

    # how long to wait at getch in tenths
    curses.halfdelay(1)

    # fix mouse bug?
    curses.mousemask(-1)

    # hide cursor
    curses.curs_set(0)

    i = 0

    while True:

        # write message at location
        scr.addstr(0, 0, code, curses.color_pair(1))

        # highlight selection
        j,y,x = getIndexCoord(i)
        scr.addstr(y, x, code[j], curses.color_pair(2))

        # show index
        I = (i % len(code.split()))
        scr.addstr(h-1, 0, 'index: %i   f w m %x %x %x %x' % (I, I//16**3, (I//16**2)%16, (I//16)%16, I%16), curses.color_pair(1))

        # print buffer to console
        scr.refresh()

        if k=='q':
            exit()
        elif k == 'KEY_DOWN':
            i += 7
        elif k == 'KEY_RIGHT':
            i += 1
        elif k == 'KEY_UP':
            i -= 7
        elif k == 'KEY_LEFT':
            i -= 1

        # take keyboard input
        try:
            k = scr.getkey()
        except:
            k = ''

        # clear the screen
        scr.clear()

wrapper(main)
