from setuptools import setup
from pip.req import parse_requirements
import pip.download

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements(
    "requirements.txt",
    session=pip.download.PipSession()
)

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='Python Lightwave RF',
    version='0.0.1',
    author='Matthew Macdonald-Wallace',
    url='https://github.com/proffalken/python-lwrf',
    download_url='https://github.com/proffalken/python-lwrf/archive/0.0.1.tar.gz',
    author_email='matt@doics.co',
    packages=['lwrf'],
    license=['LICENSE.txt'],
    description=['A Python3 Library to control LightwaveRF Devices'],
    install_requires=reqs,
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest',
        'pytest-flake8'
    ],
)
