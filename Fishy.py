# Import the required modules
import os
import time
import demon  # import the custom module (i.e demon.py)

# Define a function to write to a file and then delete it
def write_and_delete():
    
    # Open the hint file in read mode
    with open('/root/hint.txt', 'r') as hint_file:
        # Read the content of the hint file
        hint_content = hint_file.read()

    # Open the user file in write mode. This will create the file if it doesn't exist.
    with open('/home/xavir/youneedme.txt', 'w') as user_file:
        # Write the content of the hint file to the user file
        user_file.write(hint_content)

    # Sleep for 60 seconds
    time.sleep(60)

    # Open the user file in append mode
    with open('/home/xavir/youneedme.txt', 'a') as user_file:
        # Append the output of the demon.figlet() function to the user file
        user_file.write('\n' + demon.figlet())

    # Delete the user file
    os.remove('/home/xavir/youneedme.txt')

# Call the write_and_delete function
write_and_delete()