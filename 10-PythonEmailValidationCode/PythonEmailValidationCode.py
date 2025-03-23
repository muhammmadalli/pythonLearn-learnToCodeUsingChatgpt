import re  # Import the regular expression module

# Define a function to perform the email validation
def validate_email(email):
    # Define the regular expression pattern for a valid email address
    pattern = r'^[\w+\.]+@\w+\.\w+$'
    
    # Create a regular expression object and set the IgnoreCase flag to True
    myReg = re.compile(pattern, re.IGNORECASE)
    
    # Use the regular expression's search method to check if the email matches the pattern
    if myReg.search(email):
        return True  # Email is valid
    else:
        return False  # Email is not valid

# Replace "myemail@hotmail.com" with the email address you want to check
email = "myemail@hotmail.com"

# Call the validate_email function and display the result
result = validate_email(email)
print("The result of validation checking:", result)