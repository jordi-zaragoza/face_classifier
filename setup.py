import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.1'
PACKAGE_NAME = 'face_classifier'
AUTHOR = 'Jordi Zaragoza'
AUTHOR_EMAIL = 'j.z.cuffi@gmail.com'
URL = 'https://github.com/jordi-zaragoza'

LICENSE = 'MIT'
DESCRIPTION = 'This repository is used for face classification.'
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"


INSTALL_REQUIRES = [
        'matplotlib==3.3.4',
        'numpy==1.19.5',
        'tensorflow==2.9.1',
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
    include_package_data=True
)
