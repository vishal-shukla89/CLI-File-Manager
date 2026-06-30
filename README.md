# CLI File Manager

A Python command-line utility designed for system-level file and directory management. This tool provides a secure, interactive interface for standard CRUD (Create, Read, Update, Delete) operations on the local file system.

## Core Features

* **Directory Traversal:** Dynamically scans and indexes available files within the active directory using modern path traversal.
* **File I/O Operations:** Safely handles file streams for reading text data, overwriting existing files, and appending new data.
* **System-Level Execution:** Leverages OS-level commands for secure file renaming and deletion.
* **Error Handling:** Implements comprehensive exception catching and path validation to prevent execution crashes during invalid user inputs.

## Technical Specifications

* **Language:** Python 3.x
* **Architecture:** Procedural with interactive loop state
* **Core Libraries:** `pathlib`, `os`
