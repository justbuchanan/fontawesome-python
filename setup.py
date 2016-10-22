from setuptools import setup
import pypandoc
import fontawesome

REL_VERSION = '2'

setup(name='fontawesome',
      packages=['fontawesome'],
      version=fontawesome.VERSION + '-' + REL_VERSION,
      description='The Font Awesome icon set for python',
      long_description=pypandoc.convert('readme.md', 'rst'),
      license='Code: Apache License, Version 2.0, Icons: SIL OFL 1.1',
      author='Justin Buchanan',
      author_email='justbuchanan@gmail.com',
      maintainer='Justin Buchanan',
      maintainer_email='justbuchanan@gmail.com',
      url='https://github.com/justbuchanan/fontawesome-python',
      classifiers=['Environment :: Console',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.4', ],
      test_suite='nose.collector',
      tests_require=['nose', 'coverage'], )
