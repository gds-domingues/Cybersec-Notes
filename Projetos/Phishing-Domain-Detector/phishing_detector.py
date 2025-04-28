import tldextract
import whois
from datetime import datetime
from fuzzywuzzy import fuzz

# Define your list of legitimate domains
legit_domains = ['google.com', 'facebook.com', 'twitter.com']

def extract_domain(url):
    """Extract the base domain from a URL."""
    ext = tldextract.extract(url)
    return f"{ext.domain}.{ext.suffix}"

def get_domain_info(domain):
    """Retrieve WHOIS information for a given domain."""
    try:
        w = whois.whois(domain)
        return w
    except Exception as e:
        print(f"Error retrieving WHOIS info for {domain}: {e}")
        return None

def is_domain_suspicious(domain_info):
    """Check if the domain is suspicious based on its registration age."""
    if domain_info and domain_info.creation_date:
        if isinstance(domain_info.creation_date, list):
            creation_date = domain_info.creation_date[0]
        else:
            creation_date = domain_info.creation_date
        age = (datetime.now() - creation_date).days
        return age < 30  # Example threshold for new domains
    return False

def is_similar_to_legit_domain(domain, legit_domains):
    """Check if the domain is similar to any known legitimate domains."""
    for legit in legit_domains:
        similarity = fuzz.ratio(domain, legit)
        if similarity > 80:  # Example threshold for similarity
            return True
    return False

def detect_phishing(url):
    """Detect if a given URL might be a phishing domain."""
    domain = extract_domain(url)
    print(f"Checking domain: {domain}")

    domain_info = get_domain_info(domain)
    
    if is_domain_suspicious(domain_info):
        print(f"[ALERT] {domain} might be a phishing domain: Newly registered")
    
    if is_similar_to_legit_domain(domain, legit_domains):
        print(f"[ALERT] {domain} might be a phishing domain: Similar to legitimate domain")
    
    if not (is_domain_suspicious(domain_info) or is_similar_to_legit_domain(domain, legit_domains)):
        print(f"{domain} seems to be normal.")

# Example usage
if __name__ == "__main__":
    url_to_check = 'http://goog1e.com'  # Replace with the URL you want to check
    detect_phishing(url_to_check)
