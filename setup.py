from setuptools import setup, find_packages

setup(
    name='WindowsCleanner',
    version='0.1.0',
    author='Arshtyi',
    author_email='arshtyi_trantor@outlook.com',
    description='A tool for cleaning unnecessary files and optimizing Windows systems.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Arshtyi/WindowsCleanner',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # List your project dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
    ],
    python_requires='>=3.6',
)