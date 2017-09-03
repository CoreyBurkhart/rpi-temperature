from RPi import GPIO
import time
import Adafruit_DHT as dht

hum, temp = dht.read_retry(dht.DHT22, 17)
temp_in_f = round((temp * 1.8) + 32)
hum = round(hum)
print 'Temp: {0}F\nHumidity: {1}%'.format(temp_in_f, hum)
