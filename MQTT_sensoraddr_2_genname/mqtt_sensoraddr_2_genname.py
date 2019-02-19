import json
import paho.mqtt.client as mqtt

MQTT_SERVER = "localhost"
MQTT_PATH = "/home/temp_encoded"
MQTT_PORT = 1883
MQTT_KEEP_ALIVE = 60

is_connected = False

#
# define 'some' functions
#


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client_obj, userdata, flags, rc):
    global is_connected

    print("Connected with result code " + str(rc))

    if rc == 0:
        is_connected = True

    # By subscribing in on_connect() the subscriptions will be renewed in case
    # lost the connection and reconnect.
    client_obj.subscribe(MQTT_PATH)


# The callback for when a PUBLISH message is received from the server.
def on_message(client_obj, userdata, message):
    # print(message.topic + " " + str(message.payload.decode("utf-8")))

    # create thread here instead ordinary programming
    print_details(message.topic, str(message.payload.decode("utf-8")))


def print_details(topic, payload):
    print(topic + " " + payload)

    # payload = '{ "sensor_address" : "28FF32", "temperature" : "31.4" }'

    json_obj = json.loads(payload)
    print("sensor address = " + json_obj["sensor_address"])
    print("temperature = " + json_obj["temperature"])


#
# main part starts here
#


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_SERVER, MQTT_PORT, MQTT_KEEP_ALIVE)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
