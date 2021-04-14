from distutils.core import setup
from setuptools import find_packages

setup(
        name='sshlist',
        version='1.0.0',
        description='SSH Storage Automation',
        long_description_content_type='text/markdown',
        author='Syahid Nurrohim',
        author_email='syahidnurrohim@gmail.com',
        license='MIT',
        classifiers=[
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            ],
        packages=find_packages('.'),
        install_requires=['inquirer'],
        entry_points={'console_scripts': ['sshlist=sshlist.sshlist:main']}
        )

