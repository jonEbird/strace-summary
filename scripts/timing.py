#!/bin/env python

from stracesummary.timing import Timing


if __name__ == "__main__":

    # TODO: Move this into a separate function and add an entry_point to setup.py

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
        print("ln.%-7.d%6.2fs: %s" % (lineno, elapsed, line))
        if elapsed > longest:
            longest = elapsed
    print("Longest gap was %.2fs" % longest)
