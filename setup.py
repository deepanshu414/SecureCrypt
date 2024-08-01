from setuptools import setup
setup(name="SecureCrypt",
      version="1.0.0",
      description="This script encrypts or decrypts files in a specified folder using a password, records the process in an Excel report, and handles errors during encryption and decryption.",
      long_description=open('README.md').read(), 
      long_description_content_type='text/markdown',
      author="Deepanshu antil",
      packages=['SecureCrypt'],
      author_email="deepanshuantil4113@gmail.com",
      url="https://github.com/deepanshu414",
      license="MIT", 
      install_requires=['pyAesCrypt','pandas','openpyxl'])
