import os
import hashlib
import subprocess
import socket

MALWARE_SAMPLES_DIR = "malware_samples"
PCAP_FILE = "malware_traffic.pcap"

def get_file_metadata(file_path):
    """
    Get metadata information of the file.
    """
    try:
        file_stats = os.stat(file_path)
        metadata = {
            "File Name": os.path.basename(file_path),
            "File Size (bytes)": file_stats.st_size,
            "Creation Time": file_stats.st_ctime,
            "Last Access Time": file_stats.st_atime,
            "Last Modified Time": file_stats.st_mtime,
        }
        return metadata
    except Exception as e:
        print(f"Error getting file metadata: {e}")
        return None

def calculate_hash(file_path):
    """
    Calculate hash values (MD5, SHA1, SHA256) of the file.
    """
    try:
        with open(file_path, "rb") as file:
            content = file.read()
            md5_hash = hashlib.md5(content).hexdigest()
            sha1_hash = hashlib.sha1(content).hexdigest()
            sha256_hash = hashlib.sha256(content).hexdigest()
            return {
                "MD5 Hash": md5_hash,
                "SHA1 Hash": sha1_hash,
                "SHA256 Hash": sha256_hash,
            }
    except Exception as e:
        print(f"Error calculating file hash: {e}")
        return None

def analyze_file(file_path):
    """
    Analyze the file for suspicious characteristics.
    """
    metadata = get_file_metadata(file_path)
    hash_values = calculate_hash(file_path)
    suspicious_characteristics = []

    # Example: Check file extension
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension in ['.exe', '.dll']:
        suspicious_characteristics.append("Executable file")

    # Example: Check for presence of packers
    # (This is just a placeholder, actual detection would be more complex)
    if "packed" in file_path.lower():
        suspicious_characteristics.append("Packed file")

    return metadata, hash_values, suspicious_characteristics

def execute_malware(file_path):
    """
    Execute the malware in a sandboxed environment.
    """
    try:
        subprocess.run(["sandbox_command", file_path], timeout=60)
        print("Malware executed successfully in sandbox.")
    except subprocess.TimeoutExpired:
        print("Timeout: Malware execution took too long.")
    except Exception as e:
        print(f"Error executing malware: {e}")


def capture_network_traffic():
    """
    Capture network traffic using tcpdump.
    """
    try:
        # Capture network traffic and save it to a file
        subprocess.run(["tcpdump", "-i", "eth0", "-w", "malware_traffic.pcap"])
    except Exception as e:
        print(f"Error capturing network traffic: {e}")

# After capturing the traffic using tcpdump, you can process the captured packets in Python
# Use a packet parsing library like dpkt or scapy to parse the captured pcap file
# Analyze the parsed packets as needed

def process_packet(header, data):
    """
    Process captured network packet.
    """
    # Extract header information
    eth_length = 14
    eth_header = data[:eth_length]
    eth = socket.struct.unpack("!6s6sH", eth_header)
    eth_protocol = socket.ntohs(eth[2])

    # Parse IP header
    if eth_protocol == 8:
        ip_header = data[eth_length:20+eth_length]
        iph = socket.struct.unpack("!BBHHHBBH4s4s", ip_header)
        version_ihl = iph[0]
        version = version_ihl >> 4
        ihl = version_ihl & 0xF
        iph_length = ihl * 4
        ttl = iph[5]
        protocol = iph[6]
        s_addr = socket.inet_ntoa(iph[8])
        d_addr = socket.inet_ntoa(iph[9])

        # Parse TCP header
        if protocol == 6:
            tcp_header = data[iph_length + eth_length:iph_length + eth_length + 20]
            tcph = socket.struct.unpack("!HHLLBBHHH", tcp_header)
            source_port = tcph[0]
            dest_port = tcph[1]
            sequence = tcph[2]
            acknowledgment = tcph[3]
            doff_reserved = tcph[4]
            tcph_length = doff_reserved >> 4
            flags = tcph[5]
            urg = flags & 0x20
            ack = flags & 0x10
            psh = flags & 0x08
            rst = flags & 0x04
            syn = flags & 0x02
            fin = flags & 0x01

            # Print packet information
            print(f"Source IP: {s_addr}")
            print(f"Destination IP: {d_addr}")
            print(f"Source Port: {source_port}")
            print(f"Destination Port: {dest_port}")
            print(f"Protocol: TCP")
            print(f"TTL: {ttl}")
            print(f"URG: {urg}, ACK: {ack}, PSH: {psh}, RST: {rst}, SYN: {syn}, FIN: {fin}")

        # Parse UDP header
        elif protocol == 17:
            udp_header = data[iph_length + eth_length:iph_length + eth_length + 8]
            udph = socket.struct.unpack("!HHHH", udp_header)
            source_port = udph[0]
            dest_port = udph[1]
            length = udph[2]
            checksum = udph[3]

            # Print packet information
            print(f"Source IP: {s_addr}")
            print(f"Destination IP: {d_addr}")
            print(f"Source Port: {source_port}")
            print(f"Destination Port: {dest_port}")
            print(f"Protocol: UDP")
            print(f"TTL: {ttl}")

        # Parse ICMP header
        elif protocol == 1:
            icmp_header = data[iph_length + eth_length:iph_length + eth_length + 4]
            icmph = socket.struct.unpack("!BBH", icmp_header)
            icmp_type = icmph[0]
            code = icmph[1]
            checksum = icmph[2]

            # Print packet information
            print(f"Source IP: {s_addr}")
            print(f"Destination IP: {d_addr}")
            print(f"Protocol: ICMP")
            print(f"TTL: {ttl}")

        # Parse other IP protocols
        else:
            print(f"Source IP: {s_addr}")
            print(f"Destination IP: {d_addr}")
            print(f"Protocol: {protocol}")
            print(f"TTL: {ttl}")

    # Parse other Ethernet protocols
    else:
        print(f"Ethernet Protocol: {eth_protocol}")

    # Print separator for readability
    print("=" * 50)


if __name__ == "__main__":
    # Analyze a malware sample
    malware_sample_path = os.path.join(MALWARE_SAMPLES_DIR, "simplecode.py")
    if os.path.isfile(malware_sample_path):
        metadata, hash_values, suspicious_characteristics = analyze_file(malware_sample_path)

        print("\nFile Metadata:")
        for key, value in metadata.items():
            print(f"{key}: {value}")

        print("\nHash Values:")
        for key, value in hash_values.items():
            print(f"{key}: {value}")

        print("\nSuspicious Characteristics:")
        if suspicious_characteristics:
            for characteristic in suspicious_characteristics:
                print(characteristic)
        else:
            print("No suspicious characteristics found.")

        # Execute the malware
        execute_malware(malware_sample_path)

        # Capture network traffic generated by the malware
        capture_network_traffic()

    else:
        print("Malware sample not found.")
