#!/bin/env python

import os
import sys
import re
import time
import logging as log

from tracedata import TraceData

class Timing(TraceData):

    def find_gaps(self, threshold=.5):
        """Report on time deltas between successive lines taking longer than
        threshold in seconds"""
        prev = self.parse_datetime(self.beginning)
        lline = '-- beginning --'
        longest = 0

        for n, line in enumerate(self.getlines(), 1):
            now = self.parse_datetime(line)
            if now == self.epoch:
                #print 'DEBUG: skipping line: %s' % line
                continue
            sec = (now - prev).total_seconds()
            if sec > threshold:
                # Report on last line
                print "ln.%-7.d%6.2fs: %s" % (n-1, sec, lline)

            # end of loop processing
            if sec > longest:
                longest = sec
            lline = line
            prev = now

        print "Longest gap was %.2fs" % longest

if __name__ == "__main__":

    from optparse import OptionParser
    parser = OptionParser(usage="%prog [options] tracefile", version='0.1b')
    parser.add_option('-t', '--threshold', type="float", default=1.0,
                      help="Threshold to use when reporting trace data line deltas")

    (options, args) = parser.parse_args()
    if not args:
        parser.error("Missing trace datafile argument")

    tracefile = args[0]

    # Obviously prototyping
    ss = Timing(tracefile)
    ss.find_gaps(options.threshold)
