from distutils.core import setup

from download_ckan import __version__

setup(name='download_ckan',
      author='Thomas Levine',
      author_email='_@thomaslevine.com',
      description='Download data from OpenDataSoft open data platforms.',
      url='https://github.com/tlevine/download_ckan',
      packages=['download_ckan'],
      install_requires = ['picklecache'],
      tests_require = ['nose'],
      version=__version__,
      license='AGPL',
)
