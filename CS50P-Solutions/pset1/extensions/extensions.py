# Get user input, convert to lowercase, and remove leading/trailing whitespaces
x = input("File Name: ").lower().strip()

# Define file extensions
a, b, c, d, e, f, g = ".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip"

# Check if each file extension is present in the user input
if a in x:
    # If true, print the corresponding MIME type
    print("image/gif")
elif b in x:
    print("image/jpeg")
elif c in x:
    print("image/jpeg")
elif d in x:
    print("image/png")
elif e in x:
    print("application/pdf")
elif f in x:
    print("text/plain")
elif g in x:
    print("application/zip")
# If none of the specified file extensions are found
else:
    # Print a default MIME type
    print("application/octet-stream")
"""
This code takes a file name as input and checks for specific file extensions. 
Depending on the extension, it prints the corresponding MIME type. 
If none of the specified file extensions are found, it prints a default MIME type
"""