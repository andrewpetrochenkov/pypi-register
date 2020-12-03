import setuptools
import json

with open('package.json') as f:
    package_metadata = json.load(f)

with open('README.md') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name='pypi-register',
    install_requires=requirements,
    scripts=['scripts/pypi-register'],
    version=package_metadata['version'],
    description=package_metadata['description'],
    keywords=package_metadata['keywords'],
    url=package_metadata['homepage'],
    license=package_metadata['license'],
    long_description=long_description,
    long_description_content_type='text/markdown',
)
