<div align="center">

<img src="https://socialify.git.ci/deepanshu414/SecureCrypt/image?description=1&descriptionEditable=SecureCrypt%20is%20a%20robust%20tool%20for%20encrypting%20and%20decrypting%20files%20in%20specified%20directories%20using%20AES%20encryption.&font=KoHo&forks=1&issues=1&language=1&name=1&pattern=Plus&pulls=1&stargazers=1&theme=Auto" alt="SecureCrypt" width="640" height="320" />

</div>

SecureCrypt is a Python package that provides advanced encryption and decryption capabilities, allowing you to securely handle sensitive data. This documentation will guide you through the installation process, explain the features of SecureCrypt, and provide examples of how to use it.


## Table of Contents
- [Installation](#installation)
- [Features](#features)
- [Usage](#usage)
- [Contributing](#contributing)
   - [Getting Started](#getting-started)
   - [Keeping Your Fork Up to Date](#keeping-your-fork-up-to-date)
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



## Contributing


Kindly go through [CONTRIBUTING.md](CONTRIBUTING.md) to understand everything from setup to contributing guidelines.
Thank you for your interest in contributing to our project! We welcome contributions from the community to help improve and enhance our work. This guide will walk you through the process of contributing using Git commands. Also, please follow our contribution guidelines, before contributing to the project.

---
### Getting Started

To contribute to our project, follow these steps:

1. **Fork the Repository:** Click on the [Fork](https://github.com/deepanshu414/SecureCrypt/fork) button at the top right corner of the repository page. This will create a copy of the repository in your GitHub account.

2. **Clone the Repository:** Open your terminal and navigate to the directory where you want to clone the repository. Use the following command to clone the repository to your local machine:

    ```bash
    git clone https://github.com/deepanshu414/SecureCrypt
    ```

3. **Create a New Branch:** Before making any changes, create a new branch to work on. Use the following command to create a new branch:

    ```bash
    git checkout -b your-branch-name
    ```

4. **Make Changes:** Make the necessary changes to the project files using your preferred text editor or IDE.

5. **Commit Changes:** Once you have made your changes, it's time to commit them. Use the following command to commit your changes:

    ```bash
    git add .
    git commit -m "Your commit message"
    ```

6. **Push Changes:** Push your changes to your forked repository using the following command:

    ```bash
    git push origin your-branch-name
    ```

7. **Create a Pull Request:** Go to the original repository on GitHub and click on the "New Pull Request" button. Fill in the necessary details and submit your pull request.

---
### Keeping Your Fork Up to Date

To keep your forked repository up to date with the original repository, follow these steps:

1. **Add the Upstream Remote:** In your terminal, navigate to your local repository and use the following command to add the upstream remote:

    ```bash
    git remote add upstream https://github.com/deepanshu414/SecureCrypt
    ```

2. **Fetch the Latest Changes:** Use the following command to fetch the latest changes from the upstream repository:

    ```bash
    git fetch upstream
    ```

3. **Merge the Changes:** Once you have fetched the latest changes, use the following command to merge them into your local branch:

    ```bash
    git merge upstream/main
    ```

4. **Push the Changes:** Finally, push the merged changes to your forked repository using the following command:

    ```bash
    git push origin your-branch-name
    ```
---

## License

SecureCrypt is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute this package according to the terms of the license.

