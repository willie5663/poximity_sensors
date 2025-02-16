import network
import ustruct
import time

log_file = 'scan_log.csv'

# Function to log the scan results to a CSV file
def log_scan_result(mac_address, channel, rssi):
    with open(log_file, 'a') as csvfile:
        writer = csvfile.write(f"{mac_address}, {channel}, {rssi}\n")

# Function to perform the scan
def scan_network():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    # get the current time
    current_time = time.time()

    # Perform WiFi scan
    networks = wlan.scan()

    # Log each found network to the CSV
    for network in networks:
        mac_address = ':'.join(['{:02X}'.format(byte) for byte in network[1]])  # Convert the byte array to MAC address
        channel = network[2]
        rssi = network[3]  # RSSI value is the 4th element

        # Log to CSV
        log_scan_result(current_time, mac_address, channel, rssi)

# Run the network scan and log the results
scan_network()
