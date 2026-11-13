import json
import time
import random
import paho.mqtt.client as mqtt

# Kapcsolódás a postáshoz (Mosquitto) a saját gépen
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883)
client.loop_start()

seq = 0
while True:
    seq = seq + 1
    uzenet = {
        "seq": seq,
        "ts": time.time(),      # TODO: a mostani idő
        "rms": random.uniform(0.5, 1.5),     # TODO: véletlenszám 0.5 és 1.5 között
        "unit": "m/s2",
    }
    szoveg = json.dumps(uzenet)
    client.publish("ventilator/1/jellemzok", szoveg)
    print("Elküldve:", uzenet)
    time.sleep(1)