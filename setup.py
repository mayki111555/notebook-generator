from setuptools import setup, find_packages

setup(
    name='notebook_generator',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'markdown',
    ],
    entry_points={
        'console_scripts': [
            'notebook-generator=notebook_generator.cli:main'
        ]
    },
)
