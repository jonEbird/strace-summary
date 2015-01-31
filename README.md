strace Summary
==============================

The `strace` utility is incredibly useful for troubleshooting applications
within Linux. However it can generate a lot of information which can be
time consuming to analyze. This project aims to make the analysis quicker
and easier by summarizing the activity that occurred and point out well
known issues.

How to Use it
------------------------------

**Warning**: Will very likely change - In very early in development stage

Can use `timing.py` script with a trace file input. Understands different
timestamp formats as seen in a strace/ltrace `-tt` optioned output, epoch
style time from a ftrace output or basic locale format.

Pass `-t / --threshold` to control how sensitive you want to be reported:
    
    ./timing.py strace.out -t 2

Contributing
------------------------------

TODO
