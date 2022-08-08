from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("Your Bot API that you got from BotFather", use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello, I am the portfolio bot of\n Your Name\n For help about commands type or click /help")

def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :- 
    /github - To get the github link
    /linkedin - To get the LinkedIn profile
    /gmail - To write me
    /instagram - To connect with me
    other info that you want to give""")

def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text("mailto:your_email_ID")

def linkedin_url(update: Update, context: CallbackContext):
    update.message.reply_text("link to linkedIn")

def github_url(update: Update, context: CallbackContext):
    update.message.reply_text("link to github")

def instagram_url(update: Update, context: CallbackContext):
    update.message.reply_text("link to instagram")    

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)

def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry I can't recognize you, you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help)) 
updater.dispatcher.add_handler(CommandHandler('github', github_url))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedin_url))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(CommandHandler('instagram', instagram_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
