import re
import datetime
import numpy as np
from scipy.stats import zscore

# Sample system log data
system_log_entries = [
    '[2024-02-12 10:25:12] [ERROR] Failed login attempt for user "john".',
    '[2024-02-12 10:28:20] [ERROR] Failed login attempt for user "admin".',
    '[2024-02-12 10:30:45] [INFO] User "admin" logged in successfully.',
    '[2024-02-12 10:35:55] [ERROR] Failed login attempt for user "root".',
]

# Sample web server log data
web_server_log_entries = [
    '192.168.1.100 - - [12/Feb/2024:10:25:12 +0000] "GET /index.html HTTP/1.1" 200 5420',
    '192.168.1.101 - - [12/Feb/2024:10:28:20 +0000] "POST /login.php HTTP/1.1" 404 124',
    '192.168.1.102 - - [12/Feb/2024:10:30:45 +0000] "GET /index.html HTTP/1.1" 200 5420',
    '192.168.1.103 - - [12/Feb/2024:10:35:55 +0000] "GET /admin.php HTTP/1.1" 403 342',
]

# Regular expression patterns for parsing log entries
system_log_pattern = r'\[(.*?)\] \[(.*?)\] (.*)'
web_server_log_pattern = r'^(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(.*) (\S+) (\S+)" (\d{3}) (\d+)$'

def parse_system_log_entry(log_entry):
    """
    Parse a system log entry into its components: timestamp, log level, and message.
    """
    match = re.match(system_log_pattern, log_entry)
    if match:
        timestamp_str, log_level, message = match.groups()
        timestamp = datetime.datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
        return timestamp, log_level, message
    else:
        return None

def parse_web_server_log_entry(log_entry):
    """
    Parse a web server log entry into its components: IP address, timestamp, request method, status code, etc.
    """
    match = re.match(web_server_log_pattern, log_entry)
    if match:
        ip_address, _, _, timestamp_str, _, _, _, status_code, _ = match.groups()
        timestamp = datetime.datetime.strptime(timestamp_str, '%d/%b/%Y:%H:%M:%S %z')
        return ip_address, timestamp, status_code
    else:
        return None

def analyze_logs(system_logs, web_server_logs):
    """
    Analyze system logs and web server logs to detect security incidents or anomalies.
    """
    security_incidents = []

    # Failed login attempt analysis
    for log_entry in system_logs:
        timestamp, log_level, message = parse_system_log_entry(log_entry)
        if log_level == 'ERROR' and 'failed login' in message.lower():
            security_incidents.append((timestamp, 'Failed login attempt', message))

    # Unusual status code analysis
    for log_entry in web_server_logs:
        ip_address, timestamp, status_code = parse_web_server_log_entry(log_entry)
        if status_code in ['404', '403']:
            security_incidents.append((timestamp, 'Unusual status code', f'IP: {ip_address}, Status code: {status_code}'))

    # Outlier detection based on request count per IP address
    ip_addresses = [parse_web_server_log_entry(entry)[0] for entry in web_server_logs]
    unique_ip_addresses, request_counts = np.unique(ip_addresses, return_counts=True)
    z_scores = zscore(request_counts)
    outlier_indices = np.where(np.abs(z_scores) > 2)[0]  # Threshold Z-score of 2 for outliers
    for idx in outlier_indices:
        security_incidents.append((datetime.datetime.now(), 'Outlier IP Activity', f'IP: {unique_ip_addresses[idx]}, Requests: {request_counts[idx]}'))

    # Behavioral analysis (placeholder - needs more sophisticated implementation)
    # Here, we could analyze patterns of activity over time and detect deviations from normal behavior

    return security_incidents

# Analyze logs
security_incidents = analyze_logs(system_log_entries, web_server_log_entries)

# Print detected security incidents
print("Detected Security Incidents:")
for incident in security_incidents:
    print("Timestamp:", incident[0])
    print("Type:", incident[1])
    print("Message:", incident[2])
    print()
