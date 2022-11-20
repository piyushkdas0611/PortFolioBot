from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("Bot API", use_context=True)

#start message
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello, I am the portfolio bot of\n Your Name\n For help about commands type or click /help")

#help message
def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :- 
    /github - To see my other repos
    /linkedin - To see my LinkedIn page
    /gmail - To write me
    /instagram - To have a glance of my life
    /twitter - To see my views of the world issues""")

#gmail url

def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text("mailto:your_email_ID")

#linkedIn handle

def linkedin_url(update: Update, context: CallbackContext):
    update.message.reply_text("link to linkedIn")

#github_url    

def github_url(update: Update, context: CallbackContext):
    update.message.reply_text("link to github")

#instagram link

def instagram_url(update: Update, context: CallbackContext):
    update.message.reply_text("link to instagram")

#twitter link

def twitter_url(update: Update, context: CallbackContext):
  update.message.reply_text("link to twitter account")    

#update message if anyone used a wrong command

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)

#message to handle errrors

def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry I can't recognize you, you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help)) 
updater.dispatcher.add_handler(CommandHandler('github', github_url))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedin_url))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(CommandHandler('instagram', instagram_url))
updater.dispatcher.add_handler(CommandHandler('twitter', twitter_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
