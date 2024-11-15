from setuptools import setup, find_packages
import os

setup(
    name='github-repo-size-cli',  # Package name
    version='0.2.5',  # Match the installation script version
    description='A CLI tool to fetch and display the size of GitHub repositories.',
    long_description=open('README.md').read() if os.path.exists('README.md') else '',
    long_description_content_type='text/markdown',  
    author='Pezhvak',  
    author_email='m.8562.m@gmail.com',  
    url='https://github.com/pezhvak98/Github-Repo-Size-CLI',  
    packages=find_packages(),  
    py_modules=['github_repo_size'],  # Explicitly list Python modules
    install_requires=[
        'requests>=2.20.0',  # Specify a minimum version of requests
    ],
    entry_points={
        'console_scripts': [
            'grs=github_repo_size:main',  # Define the command-line entry point
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',  
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Console',
    ],
    keywords='GitHub repository size CLI tool',
    python_requires='>=3.8',  # Minimum Python version
    license='MIT',  
    include_package_data=True,  
)
