from linebot import LineBotApi
from linebot.models import TextSendMessage


CHANNEL_ACCESS_TOKEN = "jXcQzBcsPLs+sY3+FdKOgzs14ax0FCr5/2SEf83OI8vSgCiSIP7z2Yc+MqwP9ICyyIi6dQFVJQKPsR73IitC5aaHgVrla7fbQ0bslyjoZ3drUtYeV2XoGugf9gRLL6unJCYdEEpEJZZdEX636gJ/XQdB04t89/1O/w1cDnyilFU="

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

USER_ID = "Ub897c4b81f83a61395247d96fc4a6b78"

message = TextSendMessage(text="お誕生日おめでとうございます！")

line_bot_api.push_message(USER_ID, message)
