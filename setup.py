# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')


def read_requirements(requirement_file):
    with (here / requirement_file).open(mode='r', encoding='utf-8') as input_file:
        return [i.strip() for i in input_file if not i.strip().startswith('#')]


INSTALL_REQUIRES = read_requirements("requirements.txt")
TEST_REQUIRES = read_requirements("requirements_test.txt")

setup(
    name='python-exit-gracefully-example',

    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    version='1.0.0',

    # This is a one-line description or tagline of what your project does. This
    # corresponds to the "Summary" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#summary
    description='Python exit gracefully example',

    # This is an optional longer description of your project that represents
    # the body of text which users will see when they visit PyPI.
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://gitlab.com/ipsedixit-org/python-exit-gracefully-example',
    author='ipsedixit',

    # This field adds keywords for your project which will appear on the
    # project page.
    keywords='sample',

    packages=find_packages(where='python_exit_gracefully_example'),

    # Specify which Python versions you support. In contrast to the
    # 'Programming Language' classifiers above, 'pip install' will check this
    # and refuse to install the project if the version does not match. See
    # https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires
    python_requires='>=3.10, <4',

    install_requires=INSTALL_REQUIRES,
    extras_require={
        'test': TEST_REQUIRES,
    },
)
