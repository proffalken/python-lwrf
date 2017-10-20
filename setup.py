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

pkg_version = '0.0.2'
pkg_url = "https://github.com/proffalken/python-lwrf/archive/v%s.tar.gz" % (
        pkg_version
        )

setup(
    name='python-lwrf',
    version=pkg_version,
    author='Matthew Macdonald-Wallace',
    url='https://github.com/proffalken/python-lwrf',
    download_url=pkg_url,
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
