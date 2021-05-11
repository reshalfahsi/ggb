from setuptools import setup
from setuptools import find_packages

import pathlib
import os.path

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

setup(name='ggb',
      version='1.1.0',
      description='GGB Color Space in Python',
      long_description=README,
      long_description_content_type="text/markdown",
      author='Resha Dwika Hefni Al-Fahsi',
      author_email='resha.alfahsi@gmail.com',
      url='https://github.com/reshalfahsi/ggb',
      license='MIT',
      classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
      ],
      include_package_data=True,
      install_requires=['numpy', 'Pillow', 'opencv-python'],
      extras_require={
          'tests': ['pytest',
                    'pytest-cov',
                    'pytest-pep8',
                    'pytest-xdist',
                    'python-coveralls',
                    'coverage==3.7.1'],
      },
      packages=find_packages(),
      entry_points={"console_scripts": ["reshalfahsi=ggb.__main__:main"]},
)
