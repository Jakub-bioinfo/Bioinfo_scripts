import os

# Specify the directory you want to scan
directory = 'RGB_good'  # Change this to your directory path

# Specify the output file where the list of files will be saved
output_file = 'file_list.txt'

# Get a list of all .xisf files in the directory
xisf_files = [f for f in os.listdir(directory) if f.endswith('_d.xisf')]

# Save the list to a file (without "./" part and "_d")
with open(output_file, 'w') as file:
    for xisf in sorted(xisf_files):
        # Remove "_d" and extension before writing to file
        file_name = xisf.replace('_d.xisf', '')
        file.write(f"{file_name}\n")

# Print the number of XISF files in the terminal
print(f"Total number of XISF files: {len(xisf_files)}")
print(f"List of XISF files saved to {output_file}")
