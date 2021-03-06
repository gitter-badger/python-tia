# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(name='python-tia',
      version='0.0.0',
      description='tia: The generic Test Impact Analysis (TIA) preprocessor for test tools.',
      url='http://github.com/fkromer/python-tia',
      author='Florian Kromer',
      author_email='florian.kromer@mailbox.org',
      python_requires='>=3.4.0',
      license='GPLv3',
      packages=find_packages(),
      entry_points='''
          [console_scripts]
          tia=tia.cli:cli
          ''',
      classifiers=[
          'Development Status :: 1 - Planning',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Natural Language :: English',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3 :: Only',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Security',
          'Topic :: Software Development',
          'Topic :: Software Development :: Pre-processors',
          'Topic :: Software Development :: Quality Assurance',
          'Topic :: Software Development :: Testing',
          'Topic :: Software Development :: Testing :: Acceptance',
          'Topic :: Software Development :: Testing :: BDD',
          'Topic :: Software Development :: Testing :: Unit',
          'Topic :: Software Development :: Version Control :: Git',
        ],
)
