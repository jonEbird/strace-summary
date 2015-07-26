#!/bin/env python

import os

# Key import of our module
import stracesummary

datadir = os.path.join(os.path.dirname(__file__), 'data')

# On with the Tests
# --------------------------------------------------


def test_timing():
    "Can properly identify the timing gap in strace data"
    tracefile = os.path.join(datadir, 'sssd_be.strace')
    threshold = 20
    ss = stracesummary.Timing(tracefile)
    gaps = list(ss.find_gaps(threshold=threshold))
    assert len(gaps) == 1, \
        "Should have only found one gap in %s over %0.2fs long" % \
        (tracefile, threshold)
