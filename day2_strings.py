#create a variable for base API URL
base_api_url = "https://api.example.com/v1"
#create a variable for endpoint path
endpoint_path = "/users"
#combine base URL and endpoint path to create full API URL using f-string
full_api_url = f"{base_api_url}{endpoint_path}"
#Create a  variable for error message from an API response
error_message = "Error fetching user data"
#check if the word "unauthorized" is in the error message
#Print true or false
print("unauthorized" in error_message.lower())
# Convert the error message to uppercase
print(error_message.upper())
# Convert the error message to lowercase
print(error_message.lower())    
#count how many characters are in error message
print(len(error_message))
#split the error message into list of words
print(error_message.split())
#Replace "unauthorized" with "invalid credentials" in the message
print(error_message.replace("Unauthorized", "Invalid credentials"))
#strip whitespace from this messy string : "    test_user.  "
print("    test_user.  ".strip())
#check if the url starts with the "https"
#print a warning if it doesn't
if not full_api_url.startswith("https"):
    print("Warning: API URL is not secure (HTTPS).")
    
