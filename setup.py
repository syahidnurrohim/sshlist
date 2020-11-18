import PyInstaller

setup(
    name='sshlist',
    version='1.0.0',
    description='SSH Storage Automation',
    long_description_content_type='text/markdown',
    url='https://github.com/syahidnurrohim/sshlist',
    author='Syahid Nurrohim',
    author_email='syahidnurrohim@gmail.com',
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    include_package_data=True,
    install_requires=['inquirer'],
    entry_points={'console_scripts': ['sshlist=sshlist.__main__:main']}
)

