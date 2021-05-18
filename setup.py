from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='matchkraft',
  version='0.0.1',
  description='Fuzzy match company names',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Rene Tatua Castillo',
  author_email='info@matchkraft.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['matchkraft', 'machine learning', 'python'],
  packages=find_packages(),
  install_requires=[
        # use "pip install requests[security]" for taking out the warnings
        'requests>=2.8.1',
        'six>=1.10.0',
    ],
)