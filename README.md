<div align="center">

<img src="https://socialify.git.ci/deepanshu414/SecureCrypt/image?description=1&descriptionEditable=SecureCrypt%20is%20a%20robust%20tool%20for%20encrypting%20and%20decrypting%20files%20in%20specified%20directories%20using%20AES%20encryption.&font=KoHo&forks=1&issues=1&language=1&name=1&pattern=Plus&pulls=1&stargazers=1&theme=Auto" alt="SecureCrypt" width="640" height="320" />

</div>

SecureCrypt is a Python package that provides advanced encryption and decryption capabilities, allowing you to securely handle sensitive data. This documentation will guide you through the installation process, explain the features of SecureCrypt, and provide examples of how to use it.


## Table of Contents
- [Installation](#installation)
- [Features](#features)
- [Usage](#usage)
- [License](#license)

---
## Installation

To install SecureCrypt, you can use pip. Open your terminal and run the following command:

```sh
pip install SecureCrypt
```
---
## Features

SecureCrypt offers the following features:

- **Encryption**: Securely encrypt your data using advanced cryptographic techniques.
- **Decryption**: Easily decrypt your encrypted data.
- **Support for various encryption algorithms**: SecureCrypt supports a wide range of encryption algorithms, allowing you to choose the one that best suits your needs.

---
## Usage

SecureCrypt can be used in two different ways, depending on your preference. Here are the examples for both approaches:

### Approach 1: Importing the `encrypt` and `decrypt` functions

```python
from SecureCrypt import encrypt, decrypt

# Encrypting data
encrypt(current_minute,r'path_to_file',file_password)

# Decrypting data
decrypt(current_minute,r'path_to_file',file_password)
```

### Approach 2: Importing the *SecureCrypt* module

```python
import SecureCrypt

# Encrypting data
SecureCrypt.encrypt(current_minute,r'path_to_file',file_password)

# Decrypting data
SecureCrypt.decrypt(current_minute,r'path_to_file',file_password)
```

---

Make sure to replace `current_minute` with the actual data you want to encrypt or decrypt, `r'path_to_file'` with the path to the file you want to encrypt or decrypt, and `file_password` with the password you want to use for encryption or decryption.


---
## License

SecureCrypt is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute this package according to the terms of the license.

