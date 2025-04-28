# Network-Scanner
This script allows users to perform network scanning by specifying the target IP address or range and the ports to scan. It provides flexibility in output format (JSON or CSV) and handles various aspects of the scanning process, including sending packets, receiving responses, and saving results.

1. **Importing Libraries**:
    - **`scapy.all as scapy`**: This line imports the Scapy library, which is a powerful tool for network scanning and manipulation of network packets. The **`as scapy`** part aliases the library to **`scapy`**, making it easier to reference its functions and classes throughout the code.
    - **`argparse`**: Here, the argparse module is imported from Python's standard library. It allows the script to parse command-line arguments in a structured and convenient way.
    - **`json`**: The json module is imported, enabling the script to handle JSON data, including serialization and deserialization.
2. **Defining `get_arguments()` Function**:
    - This function sets up an ArgumentParser object to parse command-line arguments.
    - **`ArgumentParser(description="Network Scanner")`**: Creates an ArgumentParser object with a description indicating that it's for a network scanner.
    - **`add_argument()`**: This method defines the command-line arguments that the script expects. It specifies the target IP address or range, ports to scan, and output format.
    - **`parse_args()`**: Finally, the function parses the provided arguments and returns them for further use in the script.

```python
def get_arguments():
    # Setting up command-line argument parser
    parser = argparse.ArgumentParser(description="Network Scanner")
    parser.add_argument("target", help="Target IP address or range (CIDR notation)")
    parser.add_argument("-p", "--ports", default="1-1024", help="Ports to scan (default: 1-1024)")
    parser.add_argument("-o", "--output", choices=["json", "csv"], help="Output format (json/csv)")
    return parser.parse_args()
```

1. **Defining `scan_port(ip, port)` Function**:
    - This function scans a specific port on a given IP address.
    - It constructs a TCP SYN packet using Scapy, a powerful packet manipulation tool.
    - The **`scapy.sr1()`** function sends the packet and waits for a response with a timeout of 1 second.
    - If a response is received and it contains a TCP layer, indicating that the port is open, the function returns the port number and True. Otherwise, it returns the port number and False.

```python
def scan_port(ip, port):
    try:
        # Scanning port using TCP SYN packet
        response = scapy.sr1(scapy.IP(dst=ip)/scapy.TCP(dport=port, flags="S"), timeout=1, verbose=False)
        if response and response.haslayer(scapy.TCP):
            return port, True  # Port is open
        else:
            return port, False  # Port is closed
    except Exception as e:
        print(f"Error scanning port {port} on {ip}: {e}")
        return port, False
```

1. **Defining `scan_network(target, ports_range)` Function**:
    - This function performs a network scan to find active hosts and open ports within the specified target range.
    - It constructs an ARP request packet using Scapy to discover hosts within the target network.
    - The **`scapy.srp()`** function sends the ARP request and receives responses, indicating active hosts on the network.
    - For each active host, the function calls the **`scan_host()`** function to scan for open ports.
    - Finally, it returns a dictionary containing the scan results, with host IPs as keys and lists of open ports as values.

```python
def scan_network(target, ports_range):
    interface = "Ethernet"  # Network interface to use for scanning
    print("Scanning network...")
    # Constructing ARP request packet
    hosts = scapy.ARP(pdst=target)
    # Sending ARP request and receiving responses
    answered_list = scapy.srp(hosts, timeout=60, iface=interface, verbose=False)[0]
    scan_results = {}
    for element in answered_list:
        ip = element[1].psrc
        scan_results.update(scan_host(ip, ports_range))  # Scan open ports on each host
    print("Scan completed.")
    return scan_results
```

1. **Defining `main()` Function**:
    - This function serves as the entry point for the script and orchestrates the entire network scanning process.
    - It first parses command-line arguments using the **`get_arguments()`** function.
    - Then, it calls the **`scan_network()`** function to perform the network scan based on the provided target and ports range.
    - Depending on the specified output format (JSON or CSV), the function saves the scan results to files or prints them to the terminal.

```python
def main():
    args = get_arguments()
    target = args.target
    ports_range = list(map(int, args.ports.split("-")))
    scan_results = scan_network(target, ports_range)
    if args.output == "json":
        with open("scan_results.json", "w") as file:
            json.dump(scan_results, file, indent=4)
    elif args.output == "csv":
        with open("scan_results.csv", "w") as file:
            for ip, ports in scan_results.items():
                file.write(f"{ip},{','.join(map(str, ports))}\\n")
    else:
        for ip, ports in scan_results.items():
            print(f"IP: {ip}\\tOpen Ports: {', '.join(map(str, ports))}")

if __name__ == "__main__":
    main()
```

This breakdown explains how each part of the code contributes to the network scanning process, from parsing command-line arguments to processing scan results.
