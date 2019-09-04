from setuptools import setup

APP = ['app.py']
DATA_FILES = []
OPTIONS = {'argv_emulation': True,
 'iconfile': 'pugdebug.icns',
 'includes': ['PyQt5', 'flake8', 'Pygments']}

setup(
name="Pugdebug",
version="1.0.0",
app=APP,
data_files=DATA_FILES,
options={'py2app': OPTIONS},
setup_requires=['py2app'],
)