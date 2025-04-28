# Phishing Domain Detection

## Overview

This project aims to detect potential phishing domains by analyzing various characteristics of the domain, such as its registration date and similarity to known legitimate domains. The script uses Python libraries to extract domain information, perform WHOIS lookups, and compare domains to detect suspicious activity.

## Features

- **Domain Extraction:** Extracts the base domain from a given URL.
- **WHOIS Lookup:** Retrieves domain registration details to check the domain age.
- **Similarity Check:** Compares the domain with a list of known legitimate domains to detect potential phishing attempts.

## Requirements

The project requires the following Python libraries:

- `requests`
- `beautifulsoup4`
- `tldextract`
- `python-whois`
- `fuzzywuzzy`

You can install these libraries using `pip` and the `requirements.txt` file provided.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/phishing-domain-detection.git
   cd phishing-domain-detection
   
## Install Dependencies:
Make sure you have pip installed. Then run:
bash
Copy code
pip install -r requirements.txt
Usage
Update the Script:
Replace the placeholder URL in phishing_detection.py with the URL you want to check.

## Run the Script:
Execute the script using Python:

bash
Copy code
python phishing_detection.py
The script will analyze the URL and print whether the domain might be a phishing domain based on its registration date and similarity to known legitimate domains.

## Customization
Legitimate Domains: Modify the legit_domains list in phishing_detection.py to include more legitimate domains relevant to your needs.
Detection Criteria: Adjust thresholds and conditions in the is_domain_suspicious and is_similar_to_legit_domain functions to refine detection accuracy.
Contributing
Feel free to open issues or submit pull requests if you have suggestions for improvements or fixes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
