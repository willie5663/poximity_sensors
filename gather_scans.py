import network
import ustruct
import csv

# Function to log the scan results to a CSV file
def log_scan_result(mac_address, channel, rssi):
    with open('scan_log.csv', 'a', newline='') as csvfile:
        fieldnames = ['MAC Address', 'Channel', 'RSSI']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header if the file is empty
        csvfile.seek(0, 2)  # Move to the end of the file
        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow({'MAC Address': mac_address, 'Channel': channel, 'RSSI': rssi})

# Function to perform the scan
def scan_network():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    # Perform WiFi scan
    networks = wlan.scan()

    # Log each found network to the CSV
    for network in networks:
        mac_address = ':'.join(['{:02X}'.format(byte) for byte in network[1]])  # Convert the byte array to MAC address
        channel = network[2]
        rssi = network[3]  # RSSI value is the 4th element

        # Log to CSV
        log_scan_result(mac_address, channel, rssi)

# Run the network scan and log the results
scan_network()
