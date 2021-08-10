from linebot import LineBotApi
from linebot.models import TextSendMessage

CHANNEL_ACCESS_TOKEN = "bt+sJYlnWQ+elHFG6HqifBItSOHIrPQoeEYE0xD/B6rPFkTAWd29mL3IA9JlGjB+JKiklLDCIPV09ZvZC7Kjs6pnsIzedvjVO6z/jbibHK6ja2ftB4umloO8pJPRYt5Nmj9fRPlDUDZ/UHiatph5+wdB04t89/1O/w1cDnyilFU="
USER_ID = "9328d1fe37bfa6e2e478bfa65934b575"

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def sendmessage(text, filename1, filename2):
    messages = [filename1, filename2]
    message = TextSendMessage(text)

    line_bot_api.broadcast(messages=message, )