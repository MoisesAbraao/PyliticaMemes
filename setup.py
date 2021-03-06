from setuptools import setup

setup(
    name='Pyliticamemes',
    version='0.2.0',
    url='https://github.com/MoisesAbraao/PyliticaMemes',
    license='MIT',
    author='Moises Abraao',
    author_email='moisesabraaoso@gmail.com',
    description='zoeira com os memes da politica brasileira',
    long_description='',
    packages=['pyliticamemes'],
    install_requires=['pydub'],
    package_data={
        'pyliticamemes': ['sounds/*'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Libraries :: Python Modules'
        ]
    )
