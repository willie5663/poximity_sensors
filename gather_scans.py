import network
import time

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='ESP8266_Proximeter', password='IDM06-18-2010')

print("AP Mode Active. Connect to ESP8266_Proximeter")
print('IP Address: ', ap.ifconfig()[0])

sta = network.WLAN(network.STA_IF)
sta.active(True)

def scan_wifi():
    networks = sta.scan()
    for net in networks:
        ssid, mac, channel, rssi, authmode, hidden = net
        print(f"MAC: {mac}, RSSI: {rssi}, Channel: {channel}")

while True:
    scan_wifi()
    time.sleep(5)