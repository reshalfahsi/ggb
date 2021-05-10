from setuptools import setup
from setuptools import find_packages


setup(name='ggb',
      version='1.1.0',
      description='GGB Color Space in Python',
      author='Resha Dwika Hefni Al-Fahsi',
      author_email='resha.alfahsi@gmail.com',
      url='https://github.com/reshalfahsi/ggb',
      download_url='https://github.com/reshalfahsi/ggb/tarball/1.1.0',
      license='MIT',
      install_requires=['numpy', 'Pillow', 'opencv-python'],
      extras_require={
          'tests': ['pytest',
                    'pytest-cov',
                    'pytest-pep8',
                    'pytest-xdist',
                    'python-coveralls',
                    'coverage==3.7.1'],
      },
      packages=find_packages())
