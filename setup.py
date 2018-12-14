from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

classifiers = [
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'License :: OSI Approved :: MIT License',
]

setup(name='get_wayback_machine',
      version='0.1.0',
      description="Fetch a URL via the latest Wayback Machine Snapshot",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/jfilter/get-wayback-machine',
      author='Johannes Filter',
      author_email='hi@jfilter.de',
      license='MIT',
      packages=['get_wayback_machine'],
      install_requires=['get_retries'],
      classifiers=classifiers)
