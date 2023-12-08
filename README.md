# NoteCLI 📝

NoteCLI is a simple command-line note-taking application written in Python using SQLite for data storage. It allows users to create, edit, delete, and view notes through an easy-to-use command-line interface.

## Features 🚀

- **Add Note:** Create a new note with a title and content.
- **Delete Note:** Remove a note by specifying its position in the list.
- **Update Note:** Modify the title and/or content of an existing note.
- **Show Notes:** Display a list of all notes with their titles and content.

## Getting Started 🛠️

### Prerequisites

- Python 3.x
- SQLite

### Installation 📦

1. Clone the repository:

   ```bash
   git clone https://github.com/kom-senapati/NoteCLI.git
   ```

2. Navigate to the project directory:

   ```bash
   cd NoteCLI
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage 🚨

1. Run the application:

   ```bash
   python notecli.py
   ```

2. Use the following commands:

   - **Add a Note:**
     ```bash
     python notecli.py add --title "Note Title" --content "Note Content"
     ```

   - **Delete a Note:**
     ```bash
     python notecli.py delete --position 1
     ```

   - **Update a Note:**
     ```bash
     python notecli.py update --position 1 --title "New Title" --content "New Content"
     ```

   - **Show Notes:**
     ```bash
     python notecli.py show
     ```

## Contributing 🤝

Thank you for considering contributing to NoteCLI! To get started, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Create a pull request, and your changes will be reviewed.

## Issues 🐛

If you encounter any issues or have suggestions, please [open an issue](https://github.com/kom-senapati/NoteCLI/issues). Wait for it to be assigned, and feel free to contribute to the discussion.

## Acknowledgments 🙌

Thank you for visiting NoteCLI! Don't forget to give it a ⭐️ if you find it useful.