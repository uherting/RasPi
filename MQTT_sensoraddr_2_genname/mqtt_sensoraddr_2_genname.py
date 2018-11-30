import paho.mqtt.client as mqtt

MQTT_SERVER = "localhost"
MQTT_PATH = "/home/test"
MQTT_PORT = 1883
MQTT_KEEP_ALIVE = 60

#
# define 'some' functions
#


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # By subscribing in on_connect() the subscriptions will be renewed in case
    # lost the connection and reconnect.
    client.subscribe(MQTT_PATH)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    # more callbacks, etc

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
