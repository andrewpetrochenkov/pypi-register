import setuptools

setuptools.setup(
    name='pypi-register',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/pypi-register']
)
