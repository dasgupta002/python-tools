from telegram.ext import *
import secret

print('Bot warming up, hold on yikes.')

def start_command(update, context):
    update.message.reply_text('Type your joke to make me laugh!')

def help_command(update, context):
    update.message.reply_text('Forgot to joke, finding some potion for you.')

def custom_command(update, context):
    update.message.reply_text('You are a joke buddy :)')

def handle_response(text: str) -> str:
    if 'hello'in text  or 'hey' in text.lower():
        return 'Nice to have a chat with you!'
    
    if 'how are you' in text.lower():
        return 'I am bad, jokingly!'
    
    return 'XD, only jokes are allowed here!'

def handle_message(update, context):
    message_type = update.message.chat.type
    text = str(update.message.text).lower()

    reponse = ''
    if message_type == 'group':
        if '@MirhaloBot' in text:
            text = text.replace('@MirhaloBot', '').strip()
            response = handle_response(text)
    else:
        response = handle_response(text)

    update.message.reply_text(response)

def error(update, context):
    print('Something happened, sorry for not responding.')

if __name__ == '__main__':
    updater = Updater(secret.token, use_context = True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling(1.0)
    updater.idle()