#!/usr/bin/env python

from stracesummary.tracedata import TraceData


class Timing(object):
    """Help with timing analysis"""

    def __init__(self, filename):
        self._td = TraceData(filename)

    def find_gaps(self, threshold=0.5):
        """Identify time deltas between syscalls lines taking over threshold

        Args:
            threshold (float)

        Returns:
            generator: lineno, elapsed time (s), trace line
        """
        last_line = "-- beginning --"
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
