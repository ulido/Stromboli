from distutils.core import setup

setup(
    name='Stromboli',
    version='0.1',
    author='Ulrich Dobramysl',
    author_email='ulrich.dobramysl@gmail.com',
    packages=['stromboli'],
    scripts=['bin/lattice1d.py','bin/birthdeath.py'],
    description='Python implementation of the Next Reaction or Gillespie-type algorithm',
)
