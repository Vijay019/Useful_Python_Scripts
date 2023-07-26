import os
import re


def remove_special_chars(directory):
    # iterate over all files in directory
    for filename in os.listdir(directory):
        # check if file name contains special characters
        if re.search(r'[^\w\s\-_\.]', filename):
            # remove special characters from file name
            new_filename = re.sub(r'[^\w\s\-_\.]', '', filename)
            # rename file with new file name
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f'Renamed {filename} to {new_filename}')


# call remove_special_chars function with directory path
remove_special_chars(r'C:\Users\Vijay.Raghuwanshi\Downloads\OneDrive_1_7-24-2023')
