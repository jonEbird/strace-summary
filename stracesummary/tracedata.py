#!/usr/bin/env python

import re
import logging as log
from datetime import datetime

# regex to find datetime text & associated strptime pattern for parsing
known_datetime_patterns = (
    # standard for "strace -tt"
    ('\d+:\d+:\d+\.\d+', '%H:%M:%S.%f'),

    # ftrace uptime epoch style
    ('\d+\.\d{5}', 'epoch'),

    # Local time format
    ('[A-Z][a-z]{2} [A-Z][a-z]{2} \d+ \d+:\d+:\d+ \d{4}', '%c'),

    # Only HH:MM:SS
    ('\d+:\d+:\d+', '%H:%M:%S'),
)


class TraceData(object):
    "Manage strace output"

    def __init__(self, filename):
        try:
            self.__infh = open(filename)

            # Lets start by reading some of the beginning lines
            self.beginning = self.__infh.read(1000)
            self.__infh.seek(0)

            self.init()
            self.epoch = datetime.fromtimestamp(0)

        except (IOError, OSError) as e:
            log.error('Could not open filename "%s": %s', filename, str(e))

    def init(self):
        """Initialize the trace such as establishing datetime regexs, etc"""
        self.datetime_re = None
        for pat, strp in known_datetime_patterns:
            if re.search(pat, self.beginning, re.M):
                self.datetime_re = re.compile(pat)
                self.strptime = strp
                break

    def __iter__(self):
        """Yield lines to caller"""
        for line in self.__infh:
            yield line.rstrip()

    def parse_datetime(self, data, flags=0):
        """Use initilized datetime regex and strptime patterns to return
        first valid datetime object hit within data"""
        if self.datetime_re is None:
            return self.epoch

        hits = self.datetime_re.findall(data, flags)
        if hits:
            if self.strptime == 'epoch':
                return datetime.fromtimestamp(float(hits[0]))
            else:
                return datetime.strptime(hits[0], self.strptime)
        else:
            return self.epoch

    def datetime_parsed(self):
        """Yield parsed datetime objects with each line"""
        for line in self.__infh:
            yield self.parse_datetime(line), line.rstrip()
