import shutil
import os

# Define directories
source_dir = 'RAW'  # Directory A (source of PNG files)
dest_dir = 'RAW_good'    # Directory B (destination)
file_list = 'file_list.txt'     # Text file containing the list of file names (without "_d")

# Function to copy or move files
def copy_or_move_files(copy=True):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Read the file list
    with open(file_list, 'r') as f:
        files = f.readlines()

    for line in files:
        line = line.strip()  # Remove any leading/trailing whitespace
        # Add the .png extension
        png_file = f"{line}.png"

        # Build full source and destination paths
        source_path = os.path.join(source_dir, png_file)
        dest_path = os.path.join(dest_dir, png_file)

        if os.path.exists(source_path):
            if copy:
                shutil.copy(source_path, dest_path)
                print(f"Copied {png_file} to {dest_dir}")
            else:
                shutil.move(source_path, dest_path)
                print(f"Moved {png_file} to {dest_dir}")
        else:
            print(f"File {png_file} not found in {source_dir}")


# To copy files, set `copy=True`, to move files, set `copy=False`
copy_or_move_files(copy=True)

