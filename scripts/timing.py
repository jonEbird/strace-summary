#!/bin/env python

from stracesummary.tracedata import TraceData


class Timing(object):
    """Help with timing analysis"""

    def __init__(self, filename):
        self._td = TraceData(filename)

    def find_gaps(self, threshold=.5):
        """Identify time deltas between syscalls lines taking over threshold

        Args:
            threshold (float)

        Returns:
            generator: lineno, elapsed time (s), trace line
        """
        last_line = '-- beginning --'
        prev = None

        for n, dt_data in enumerate(self._td.datetime_parsed(), 1):
            now, line = dt_data
            if prev:
                delta = (now - prev).total_seconds()
                if delta > threshold:
                    yield n - 1, delta, last_line

            # end of loop processing
            last_line = line
            prev = now

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
    longest = 0
    for lineno, elapsed, line in ss.find_gaps(options.threshold):
        print "ln.%-7.d%6.2fs: %s" % (lineno, elapsed, line)
        if elapsed > longest:
            longest = elapsed
    print "Longest gap was %.2fs" % longest
