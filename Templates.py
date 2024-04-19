ERROR_MESSAGE = ()

def error():
    print(ERROR_MESSAGE)
    quit()

""" 
Prompts the user with a certian message to input something
"""
def get_user_input(input_message):
    try:
        user_input = input(input_message)
        return user_input
    except:
        error()
        
"""
Returns the text of a file from a give filepath
"""
def get_file(filepath):
    #Attempt to open the file, but if file couldn't be found FileNotFoundError is thrown 
    try:
        #Open the file and return its contents
        with open(filepath, "r") as input_file:
            return input_file.read()
    except FileNotFoundError:
       error()
       
""" 
Writes to a given file path
If the file is not found, it creates the file 
"""
def write_to_output_file(text, file_name):
    with open(file_name, "w") as file:
        file.write(text)