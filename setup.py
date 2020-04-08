#!/usr/bin/env python

from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

try:
    scripts = ['scripts/%s' % f for f in os.listdir('scripts') if f != "dummy.py"]
except OSError:
    scripts = []

version = "0.1.0"

setup(name='strace-summary',
      description="Help summarize strace data",
      long_description=README,
      classifiers=[
          "Development Status :: 4 - Beta",
      ],
      keywords='strace sysadmin linux',
      author="Jon Miller",
      author_email="jonEbird@gmail.com",
      url="https://github.com/jonEbird/strace-summary",
      license="Apache",
      version=version,
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      scripts=scripts,
      setup_requires=["flake8", "pytest-runner", "pytest"],
      dependency_links=[],
      tests_require=['pytest', 'coverage'],
      zip_safe=True,
      install_requires=[],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
