try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
  'description': 'Python Skeleton',
  'author': 'Aminu Kano',
  'url': 'https://github.com/AminuSufi585/python-skeleton',
  'download_url': 'git@github.com:AminuSufi585/python-skeleton.git',
  'author_email': 'aminukano585@gmail.com',
  'version': 'v1.0',
  'install_requires': ['nose'],
  'packages': ['NAME'],
  'scripts': [],
  'name': 'python-skeleton'
}

setup(**config)