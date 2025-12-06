import paho.mqtt.client as mqtt
import json
import time

broker_address = "localhost"
port = 1883

student_name = "SURAJ KAMATAM" 
unique_id = "42130578" 

topic = "home/SURAJ-KAMATAM/sensor" 

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "StudentScript")
client.connect(broker_address, port)

print(f"Connected! Publishing to {topic}...")

while True:
    payload = {
        "student_name": student_name,
        "unique_id": unique_id,
        "temperature": 25,        
        "humidity": 60,           
        "vibration": "Normal"     
    }

    client.publish(topic, json.dumps(payload))
    
    print(f"Sent: {payload}")
    time.sleep(5)