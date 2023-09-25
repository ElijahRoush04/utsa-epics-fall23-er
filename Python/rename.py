import os

# Specify the folder path
folder_path = r'C:\\Users\\elija\\OneDrive\\Desktop\\python'

# Define the prefix for the new filenames
prefix = 'UTSA'

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Sort the files to ensure they are in the correct order
files.sort()

# Initialize a counter for numbering
counter = 1

# Iterate through the files and rename only the .jpg files
for filename in files:
    # Check if the file has a .jpg extension
    if filename.endswith('.jpg'):
        # Create the new filename by combining the prefix and counter
        new_filename = f"{prefix}{counter}.jpg"
        
        # Construct the full path to the old and new filenames
        old_filepath = os.path.join(folder_path, filename)
        new_filepath = os.path.join(folder_path, new_filename)
        
        # Rename the file
        os.rename(old_filepath, new_filepath)
        
        # Increment the counter
        counter += 1

print("Files renamed successfully.")