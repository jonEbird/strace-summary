strace Summary
==============

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

Pass `-t / --threshold` to control how sensitive you want to be reported::

    timing.py strace.out -t 2


Development Setup
-----------------

For development, the dependent modules are kept in the `requirements-tests.txt`
file and will be installed within your virtualenv when you run::

     pip install -e .

Keep the `requirements.txt` up to date with required modules.

Development Testing
-------------------

We are using pytest_ for testing. To initiate the full tests, after you've
naturally setup your virtualenv and installed the required packages, you'd
run::

    python setup.py pytest

Or just::

    pytest

They hopefully all pass. If not, you can visit the individual test file to see
how and what it was trying to do within the `tests` directory.

.. _pytest: https://docs.pytest.org/en/latest/
