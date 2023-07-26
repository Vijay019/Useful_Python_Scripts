**README.md**

# File Name Special Characters Remover

This is a simple Python script that removes special characters from file names within a given directory. The script scans all the files in the specified directory and renames any file that contains special characters. The special characters are defined as any non-alphanumeric characters, spaces, hyphens, underscores, and dots.

## Prerequisites

- Python 3.x installed on your system.

## How to Use

1. Clone this repository to your local machine or download the `remove_special_chars.py` file.

2. Ensure you have Python 3.x installed on your computer.

3. **Important Note**: Before running the script, make sure to create a backup of the directory containing the files you want to process. Renaming files can potentially cause data loss if not used carefully.

4. Open a terminal or command prompt and navigate to the directory where the `remove_special_chars.py` file is located.

5. Run the script by executing the following command:

```bash
python remove_special_chars.py
```

6. The script will prompt you to enter the path of the directory you want to process. Provide the full path to the target directory and press `Enter`.

7. The script will iterate through all the files in the specified directory. If it finds a file with special characters in its name, it will remove those characters and rename the file.

8. The script will display the original and new file names for each renamed file.

9. Once the process is complete, check the specified directory to ensure that the file names have been modified as expected.

## Important Note

- Use this script with caution, as renaming files can potentially cause data loss or make files inaccessible if not used correctly.

- It is highly recommended to create a backup of the directory before running the script to avoid any unintentional data loss.

- The script uses regular expressions to identify and remove special characters from file names. If you need to modify the set of characters to be removed, you can edit the regular expression in the script.

## Contribution

If you find any issues with the script or want to enhance its functionality, feel free to create a pull request or raise an issue in this repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.