[file_manager] is a lightweight and efficient Python tool designed to simplify file and directory management. Unlike other libraries, it uses a secure deletion system that avoids common Windows permission locks (such as those caused by VS Code) by using the Recycle Bin.

- Features

Quick Creation: Creates folders and files with built-in name validation.

Secure Deletion: Implements send2trash to prevent "Access Denied" errors and allow file recovery.

Smart Renaming: Allows you to rename and move files with a single function.

Path Management: Allows you to work in the current directory or easily specify absolute paths.

- Installation

You can install this library directly from PyPI using pip:

pip install [file-manager-starlink]

- Requirements

Python 3.7+

Dependencies: send2trash

- Contributions

Contributions are welcome! If you have ideas for improving the library:

Fork the project.

Create a branch for your improvement (git checkout -b feature/Improvement).

Commit your changes (git commit -m 'Improvement added').

Push the changes to the branch (git push origin feature/Improvement).

Open a pull request.

- LICENSE
This project is licensed under the MIT License. See the LICENSE file for details.
