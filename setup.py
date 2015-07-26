#!/bin/env python

from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

# Cool trick to automatically pull in install_requires values directly from
# your requirements.txt file but you need to have pip module available
try:
    from pip.req import parse_requirements
    try:
        # Newer versions of pip need a session object when parsing requirements.
        from pip.download import PipSession
        install_reqs = parse_requirements(os.path.join(here, 'requirements.txt'),
                                          session=PipSession())
    except ImportError:
        # Must be an older version of pip
        install_reqs = parse_requirements(os.path.join(here, 'requirements.txt'))

    # reqs is a list of requirement
    # e.g. ['django==1.5.1', 'mezzanine==1.4.6']
    reqs = [str(ir.req) for ir in install_reqs]
except Exception as e:
    print "Failed to parse requirements: " + str(e)
    # I suggest you install pip on your system so you don't have to
    # manually update this list along with your requirements.txt file
    reqs = []

try:
    scripts = ['scripts/%s' % f for f in os.listdir('scripts') if f != "dummy.py"]
except OSError:
    scripts = []

# By requiring the setuptools_version_command package we can specify our
# version via the version_command= argument. The version is determined from your git tags.
setup_extra = {'version_command': ('git describe --tags --dirty', 'pep440-git')}


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
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      scripts=scripts,
      # Note an explicit pep8 version is required here in order for flake8 to
      # to work (as it has specific version requirements that are not directly
      # specified). Hopefully this will be resolved in the future.
      setup_requires=["setuptools_git", "setuptools_version_command",
                      "flake8", "pep8 == 1.5.7", "nose"],
      dependency_links=[],
      tests_require=['nose', 'coverage'],
      zip_safe=True,
      install_requires=reqs,
      entry_points="""
      # -*- Entry points: -*-
      """,
      **setup_extra
      )
