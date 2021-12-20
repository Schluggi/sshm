import setuptools

with open('README.md') as readme:
    long_desc = readme.read()

setuptools.setup(
    name='sshm',
    version='0.1.0',
    python_requires='>=3.6',
    scripts=['sshm'],
    author='Lukas Schulte-Tickmann',
    author_email='github@das-it-gesicht.de',
    description='Simple ssh menu',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url='https://github.com/Schluggi/sshm',
    project_urls={
        'Source': 'https://github.com/Schluggi/sshm',
        'Tracker': 'https://github.com/Schluggi/sshm/issues',
        'Funding': 'https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=KPG2MY37LCC24&source=url'
    },
    packages=setuptools.find_packages(),
    install_requires=[
        'sshconf',
        'whiptail-dialogs'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
    ]
)