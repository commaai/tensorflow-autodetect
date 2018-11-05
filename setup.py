import os
from setuptools import setup

version = os.getenv('VERSION', '1.10.1')

setup(
    name='tensorflow-autodetect',
    version=version,
    url='https://github.com/commaai/tensorflow-autodetect',
    author='comma.ai',
    author_email='',
    license='MIT',
    long_description='Auto-detect tensorflow or tensorflow-gpu package based on nvidia driver being installed',
    keywords='tensorflow tensorflow-gpu',
    install_requires=[
        ('tensorflow-gpu' if os.path.exists('/proc/driver/nvidia/version') else 'tensorflow') + '==' + version,
    ],
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
