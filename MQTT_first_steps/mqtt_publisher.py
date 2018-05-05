import paho.mqtt.publish as publish

MQTT_SERVER = "localhost"
MQTT_PATH = "/home/test"

publish.single(MQTT_PATH, "Hello World!", hostname=MQTT_SERVER)
