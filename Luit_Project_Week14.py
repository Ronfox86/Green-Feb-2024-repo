import os

# Get the current working directory
current_directory = os.getcwd()

# List all files in the current working directory
file_list = os.listdir(current_directory)

# Initialize an empty list to hold the file information
file_info_list = []

# Loop through the files and gather their information
for file_name in file_list:
    # Get the full path to the file
    full_path = os.path.join(current_directory, file_name)
    
    # Check if it is a file (not a directory)
    if os.path.isfile(full_path):
        # Get the size of the file in bytes
        file_size = os.path.getsize(full_path)
        
        # Create a dictionary with the file's name and size
        file_info = {
            "file_name": file_name,
            "file_size": file_size  # File size in bytes
        }
        
        # Add the dictionary to the list
        file_info_list.append(file_info)

# Print the list of file information
print(file_info_list) 
