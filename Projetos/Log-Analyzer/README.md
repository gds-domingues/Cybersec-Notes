# Log-Analyzer
It analyzes log types to detect security incidents or anomalies such as failed login attempts and unusual status codes.

# Log Analysis

### **Importing Necessary Libraries**

```python
import re
import datetime
import numpy as np
from scipy.stats import zscore
```

- This section imports required libraries:
    - **`re`**: Regular expression library for parsing log entries.
    - **`datetime`**: Library for handling dates and times.
    - **`numpy`**: Library for numerical computing.
    - **`scipy.stats`**: Library for statistical functions, including **`zscore`** for calculating Z-scores.

### **Sample Log Data**

```python
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
```

- This section defines sample log entries for system logs and web server logs for demonstration purposes.

### **Regular Expression Patterns**

```python
# Regular expression patterns for parsing log entries
system_log_pattern = r'\\[(.*?)\\] \\[(.*?)\\] (.*)'
web_server_log_pattern = r'^(\\S+) (\\S+) (\\S+) \\[([\\w:/]+\\s[+\\-]\\d{4})\\] "(.*) (\\S+) (\\S+)" (\\d{3}) (\\d+)$'
```

- These regular expression patterns define the structure of log entries for system logs and web server logs. They are used to extract relevant information from log entries.

### **Parsing Functions**

```python
def parse_system_log_entry(log_entry):
    """
    Parse a system log entry into its components: timestamp, log level, and message.
    """
    # Code for parsing system log entries
```

- This function **`parse_system_log_entry`** parses a system log entry into its components: timestamp, log level, and message.

```python
def parse_web_server_log_entry(log_entry):
    """
    Parse a web server log entry into its components: IP address, timestamp, request method, status code, etc.
    """
    # Code for parsing web server log entries
```

- This function **`parse_web_server_log_entry`** parses a web server log entry into its components: IP address, timestamp, request method, status code, etc.

### **Analysis Function**def analyze_logs(system_logs, web_server_logs):

```
"""
Analyze system logs and web server logs to detect security incidents or anomalies.
"""
# Code for analyzing logs and detecting security incidents/anomalies
```

- This function **`analyze_logs`** analyzes system logs and web server logs to detect security incidents or anomalies.

### **Outlier Detection**

```python
    # Outlier detection based on request count per IP address
    ip_addresses = [parse_web_server_log_entry(entry)[0] for entry in web_server_logs]
    unique_ip_addresses, request_counts = np.unique(ip_addresses, return_counts=True)
    z_scores = zscore(request_counts)
    outlier_indices = np.where(np.abs(z_scores) > 2)[0]  # Threshold Z-score of 2 for outliers
    for idx in outlier_indices:
        security_incidents.append((datetime.datetime.now(), 'Outlier IP Activity', f'IP: {unique_ip_addresses[idx]}, Requests: {request_counts[idx]}'))
```

- This section calculates the Z-scores for the request counts per IP address in the web server logs and flags entries with Z-scores above a certain threshold as outliers.

### **Security Incidents**

```python
# Print detected security incidents
print("Detected Security Incidents:")
for incident in security_incidents:
    print("Timestamp:", incident[0])
    print("Type:", incident[1])
    print("Message:", incident[2])
    print()
```

- This section prints the detected security incidents.
