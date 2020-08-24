from setuptools import setup

INSTALL_REQUIRES = [
    ]

def doSetup(install_requires):
  setup(
      name='docstring_expander',
      version='0.1',
      author='Joseph L. Hellerstein',
      author_email='jlheller@uw.edu',
      url='https://github.com/joseph-hellerstein/docstring_expander.git',
      description='Enables intellisense for **kwargs',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      packages=['docstring_expander'],
      package_dir={'docstring_expander':
          'docstring_expander'},
      install_requires=install_requires,
      include_package_data=True,
      )


if __name__ == '__main__':
  doSetup(INSTALL_REQUIRES)
