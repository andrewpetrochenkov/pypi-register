import setuptools
import json

with open('package.json') as f:
    package_metadata = json.load(f)

with open('README.md') as f:
    long_description = f.read()

setuptools.setup(
    name='pypi-register',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/pypi-register'],
    version=package_metadata['version'],
    description=package_metadata['description'],
    keywords=package_metadata['keywords'],
    url=package_metadata['homepage'],
    license=package_metadata['license'],
    long_description=long_description,
    long_description_content_type='text/markdown',
)
