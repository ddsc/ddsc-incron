from setuptools import setup

version = '0.1dev'

long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CREDITS.rst').read(),
    open('CHANGES.rst').read(),
    ])

install_requires = [
    'celery',
    'ddsc-logging',
    'setuptools',
    ],

tests_require = [
    'coverage',
    'nose',
    ]

setup(name='ddsc-incron',
      version=version,
      description="DDSC library to be used with the inotify cron system",
      long_description=long_description,
      # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[],
      keywords=[],
      author='Shaoqing Lu',
      author_email='S.Lu@fugro.nl',
      url='',
      license='MIT',
      packages=['ddsc_incron'],
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require={'test': tests_require},
      entry_points={
          'console_scripts': [
              'notify = ddsc_incron.notify:main',
          ]},
      )
