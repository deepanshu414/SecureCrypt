from setuptools import setup
setup(name="SecureCrypt",
      version="1.0.2",
      description="SecureCrypt is a robust tool for encrypting and decrypting files in specified directories using AES encryption. It includes error handling and generates detailed Excel reports on the encryption and decryption processes.",
      long_description=open('README.md').read(), 
      long_description_content_type='text/markdown',
       author="Deepanshu antil",
      maintainer="Deepanshu antil",
      packages=['SecureCrypt'],
      author_email="deepanshuantil4113@gmail.com",
      url="https://github.com/deepanshu414/SecureCrypt",
      license="MIT", 
      install_requires=['pyAesCrypt','pandas','openpyxl'])
