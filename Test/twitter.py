from twython import Twython
from gpiozero import Button
from time import sleep
button = Button(4)
consumer_key = 'VD9uUIdeYYaAfhiEVFL1185DZ'
consumer_secret = 'kofk91vXJkFlsqbNLh3s7GUbuTOzqd1JpNpFA9qX2mDQTR6rhG'
access_token = '1141880993487495173-g1WOpZ4yrC8dco40AhLGnouj4fqNjW'
access_token_secret = 'tyuG1Nm3VNCQrJYv3HsmslYBIysZ0ibJCNTPqYsJsuoA1'

twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)
while True:
    if not button.is_pressed:
        message = input("What do you want to tweet?")
        print(message)
        twitter.update_status(status=message)
        break
        