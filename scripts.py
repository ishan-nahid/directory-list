import os

def list_files_and_folders(directory, output_file):
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk(directory):
            # Calculate the depth level of the current directory
            level = root.replace(directory, '').count(os.sep)
            indent = ' ' * 4 * (level)
            f.write(f'{indent}{os.path.basename(root)}/\n')
            # Indent for files
            subindent = ' ' * 4 * (level + 1)
            for file in files:
                f.write(f'{subindent}{file}\n')

if __name__ == "__main__":
    # Get the directory and output file path from user
    directory = '' # directory you want to see
    output_file = '' # what would be the output file name
    # List the files and folders
    list_files_and_folders(directory, output_file)
    print(f"List of files and folders has been saved to {output_file}")
