import paho.mqtt.client as mqtt # import the mqtt library
import time # import for delay
import aiy.voice.tts # import the text to speech library
import sys 


def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)
    if "speak" in str(message.payload.decode("utf-8")):
        text_speak = str(message.payload.decode("utf-8")).replace('speak', '', 1)
        aiy.voice.tts.say(text_speak,volume=20)


def on_log(client, userdata, level, buf):
    print("log: ", buf)


def main():
    broker_address = "io.adafruit.com"
    print("creating new instance")
    client = mqtt.Client("AIY_VOICE_KIT")  # create new instance
    client.on_message = on_message  # attach function to callback
    client.on_log = on_log

    print("connecting to broker")
    client.username_pw_set("fkurt97","aio_TnJU484v2O6PhKxgz46yvUBEagf5")
    client.connect(broker_address,1883,60)  # connect to broker
    client.loop_start()
    print("Subscribing to topic", "fkurt97/feeds/AIY")
    client.subscribe("fkurt97/feeds/AIY", 0)
    client.loop_forever()  # start the loop

main()
