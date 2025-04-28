# Importing necessary libraries
import scapy.all as scapy  # Importing Scapy for network scanning
import argparse  # Importing argparse for command-line argument parsing
import json  # Importing json for JSON file handling

def get_arguments():
    # Setting up command-line argument parser
    parser = argparse.ArgumentParser(description="Network Scanner")
    parser.add_argument("target", help="Target IP address or range (CIDR notation)")
    parser.add_argument("-p", "--ports", default="1-1024", help="Ports to scan (default: 1-1024)")
    parser.add_argument("-o", "--output", choices=["json", "csv"], help="Output format (json/csv)")
    return parser.parse_args()

def scan_port(ip, port):
    try:
        # Attempting to scan a specific port on the target IP
        print(f"Scanning port {port} on {ip}")
        src_port = 12345  # Source port for sending packets
        response = scapy.sr1(scapy.IP(dst=ip)/scapy.TCP(sport=src_port, dport=port, flags="S"), timeout=1, verbose=False)
        print(f"Response: {response}")  # Debugging: Printing the response
        if response and response.haslayer(scapy.TCP):
            print(f"Port {port} is open on {ip}")
            return port, True  # Returning port number and True if open
        else:
            print(f"Port {port} is closed on {ip}")
            return port, False  # Returning port number and False if closed
    except Exception as e:
        print(f"Error scanning port {port} on {ip}: {e}")
        return port, False  # Returning port number and False if error occurs

def scan_host(ip, ports):
    # Scanning open ports on a specific host
    print(f"Scanning ports on host {ip}")
    open_ports = []
    for port in range(ports[0], ports[1] + 1):
        result = scan_port(ip, port)
        if result[1]:
            open_ports.append(result[0])
    print(f"Open ports on host {ip}: {open_ports}")
    return {ip: open_ports}  # Returning a dictionary with host IP and open ports

def scan_network(target, ports_range):
    # Scanning the entire network to find active hosts and open ports
    interface = "Ethernet"  # Network interface to use for scanning
    print("Scanning network...")
    hosts = scapy.ARP(pdst=target)
    answered_list = scapy.srp(hosts, timeout=60, iface=interface, verbose=False)[0]
    print("ARP responses:", answered_list)  # Debugging: Printing the list of ARP responses

    scan_results = {}
    for element in answered_list:
        ip = element[1].psrc
        try:
            scan_results.update(scan_host(ip, ports_range))
        except Exception as e:
            print(f"Error scanning {ip}: {e}")

    print("Scan completed.")
    return scan_results  # Returning a dictionary with scan results

def main():
    # Main function to execute the network scanning process
    args = get_arguments()
    target = args.target
    ports_range = list(map(int, args.ports.split("-")))

    print(f"Scanning target: {target}")
    print(f"Scanning ports: {ports_range[0]}-{ports_range[1]}")
    print(f"Output format: {args.output}")

    scan_results = scan_network(target, ports_range)
    print("Scan results:", scan_results)  # Debugging: Printing the scan results

    if args.output == "json":
        # Saving scan results to a JSON file
        with open("scan_results.json", "w") as file:
            json.dump(scan_results, file, indent=4)
        print("Results saved to 'scan_results.json'")
    elif args.output == "csv":
        # Saving scan results to a CSV file
        with open("scan_results.csv", "w") as file:
            for ip, ports in scan_results.items():
                file.write(f"{ip},{','.join(map(str, ports))}\n")
        print("Results saved to 'scan_results.csv'")
    else:
        # Printing scan results to the terminal
        for ip, ports in scan_results.items():
            print(f"IP: {ip}\tOpen Ports: {', '.join(map(str, ports))}")

if __name__ == "__main__":
    main()
