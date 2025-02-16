import network
import time

# Function to log the scan results to a CSV file
def log_scan_result(scan_time, mac_address, channel, rssi):
    with open('scan_log.csv', 'a') as csvfile:  # Open in append mode
        csvfile.write(f"{scan_time},{mac_address},{channel},{rssi}\n")  # Write data directly

# Function to perform the scan continuously
def scan_network():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    while True:  # Infinite loop to keep scanning
        current_time = time.time()  # Get time since boot

        print(f"Scanning at {current_time}...")  # Print before each scan
        networks = wlan.scan()  # Perform WiFi scan

        # Log each found network to the CSV
        for net in networks:
            mac_address = ':'.join(['{:02X}'.format(byte) for byte in net[1]])  # Convert bytes to MAC address
            channel = net[2]
            rssi = net[3]  # RSSI value

            # Log to CSV
            log_scan_result(current_time, mac_address, channel, rssi)

        print(f"Scan complete at {current_time}, {len(net)} devices found.")  

        time.sleep(5)  # Wait 5 seconds before scanning again (adjust as needed)

# Run the continuous network scan
scan_network()
