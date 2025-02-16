import network

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='ESP8266_Proximeter', password='IDM06-18-2010')


print("AP Mode Active. Connect to ESP8266_Proximeter")
print('IP Address: ', ap.ifconfig()[0])