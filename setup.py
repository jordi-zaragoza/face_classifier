import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.8'
PACKAGE_NAME = 'face_classify'
AUTHOR = 'Jordi Zaragoza'
AUTHOR_EMAIL = 'j.z.cuffi@gmail.com'
URL = 'https://github.com/jordi-zaragoza'

LICENSE = 'MIT'
DESCRIPTION = 'This repository is used for face classification.'
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"


INSTALL_REQUIRES = [
        'matplotlib>=3.0',
        'numpy>=1.8',
        'tensorflow>=2.6',
        'face_recognition>=1.3.0'
      ]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    package_data={'face_classify': ['model/*']},
    include_package_data=True
)
