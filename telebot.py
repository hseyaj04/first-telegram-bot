import telebot
import requests


bot_token = "6933167161:AAFHapG3jme_rjHXOy0fIcnt4DbqX0rfgXA"


brainshop_api_key = "5xWG4vXjOtAUXi5I"


bot = telebot.TeleBot(bot_token)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_message = message.text

    
    brainshop_url = (f"http://api.brainshop.ai/get?bid=181435&key=5xWG4vXjOtAUXi5I&uid=1&msg={user_message}" )
    payload = {
        "apikey": brainshop_api_key,
        "message": user_message
    }

   
    try:
        response = requests.post(brainshop_url, json=payload)
        response.raise_for_status() 

        brainshop_response = response.json()["cnt"] 

       
        bot.send_message(message.chat.id, brainshop_response)
    except requests.exceptions.RequestException as e:
        
        error_message = f"An error occurred: {e}"
        bot.send_message(message.chat.id, error_message)



bot.polling()
