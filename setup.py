from setuptools import setup


setup(
  name='m42pl-kvstores',
  author='@jpclipffel',
  url='https://github.com/jpclipffel/m42pl-kvstores',
  version='1.0.0',
  packages=['m42pl_kvstores',],
  install_requires=[
    'aioredis==1.3.1',
  ]
)
