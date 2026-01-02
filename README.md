PROJECT TITLE: Automated File System Organizer

OVERVIEW This is a robust backend automation tool designed to optimize local file storage. It addresses the common issue of unstructured data in directories (like the Downloads folder) by implementing an intelligent sorting algorithm. The script scans file metadata in real-time and moves files into categorized sub-directories based on their extensions, ensuring a clean and organized digital workspace.

KEY FEATURES

Intelligent Sorting Logic: Uses a dictionary-based mapping system to categorize file types (e.g., Images, Documents, Scripts) with high efficiency.

Safe File Handling: Implements defensive programming by verifying destination paths before execution to prevent data loss or overwrite errors.

Scalability: Capable of processing and organizing hundreds of files in milliseconds using optimized system calls.

Cross-Platform Compatibility: Built using standard libraries that function correctly on Windows, Linux, and macOS environments.

TECHNICAL STACK

Language: Python 3.x

Core Modules: os (Operating System Interface), shutil (High-level File Operations)

Concepts: Scripting, File I/O, Error Handling, Automation.

HOW IT WORKS The script iterates through the target directory, extracts the file extension using path manipulation, looks up the corresponding category in the rules set, creates the necessary folder if it does not exist, and safely moves the file using shell utilities.
