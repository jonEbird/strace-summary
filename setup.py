#!/usr/bin/env python

from setuptools import setup, find_packages
import os
import re
import logging
from typing import List

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.rst")).read()


def parse_requirements(fpath: str) -> List[str]:
    """Parse a requirements.txt style file and return the dependencies

    Only real feature supported is a recursive nature of allowing the file to support a
    '-r otherfile' type syntax.
    """
    comment_re = re.compile(r"^\s*#")
    other_req_re = re.compile(r"^\s*[-]r\s+(.*?)\s*$")
    reqs = []
    try:
        with open(fpath) as fh:
            for line in fh:
                if comment_re.match(line):
                    continue
                # Other requirements file?
                m = other_req_re.match(line)
                if m:
                    reqs += parse_requirements(m.group(1))
                    continue
                # lastly assume just a normal requirement
                reqs.append(line.strip())
    except (IOError, OSError) as e:
        logging.error("Could not read '%s' for requirements: %s", fpath, e)
        raise

    return reqs


try:
    scripts = ["scripts/%s" % f for f in os.listdir("scripts") if f != "dummy.py"]
except OSError:
    scripts = []

version = "0.1.0"

setup(
    name="strace-summary",
    description="Help summarize strace data",
    long_description=README,
    classifiers=["Development Status :: 4 - Beta",],
    keywords="strace sysadmin linux",
    author="Jon Miller",
    author_email="jonEbird@gmail.com",
    url="https://github.com/jonEbird/strace-summary",
    license="Apache",
    version=version,
    packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
    include_package_data=True,
    scripts=scripts,
    setup_requires=["flake8", "pytest-runner", "pytest"],
    dependency_links=[],
    tests_require=parse_requirements("requirements-test.txt"),
    zip_safe=True,
    install_requires=parse_requirements("requirements.txt"),
    entry_points="""
      # -*- Entry points: -*-
      """,
)
