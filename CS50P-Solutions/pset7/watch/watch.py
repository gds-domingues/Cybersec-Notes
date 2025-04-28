import re

def main():
    # Prompt the user for HTML input and print the parsed YouTube video URL
    html = input("HTML: ").strip()
    print(parse(html))

def parse(s):
    try:
        # Use regular expression to find the YouTube video ID from the HTML string
        url: re.Match[str] = re.search('(?<=embed\/).*?(?=")', s)

        # Construct and return the YouTube video URL
        return f"https://youtu.be/{url.group(0)}"
    except Exception:
        # Return None if the video ID extraction fails
        return None

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()

"""
This script allows users to input HTML containing an embedded YouTube video, and it attempts to extract the video ID using a regular expression. 
If successful, it constructs the corresponding YouTube video URL and prints it. If the extraction fails or encounters an exception, the script returns None. 
The use of exception handling ensures robustness when dealing with potential errors during the extraction process.
"""