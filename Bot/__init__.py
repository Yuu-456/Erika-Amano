import os, sys, logging
from pyrogram import Client 


#<-----------LOGGING------------>
logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger("Bot by @soheru")
LOG.setLevel(level=logging.INFO)
#<-----------Variables-------------->
LOG.info('❤️ Checking Bot Variables.....')
TRIGGERS = os.environ.get("TRIGGERS", "/ !").split(" ")
BOT_TOKEN = os.environ.get('BOT_TOKEN', '5789003155:AAGQD7tQTdWK8Avz9RI80290cYo2qHnDCAs') #BOT Token Add
API_ID = int(os.environ.get('API_ID', 17789594)) #Telgram Api id
APP_HASH = os.environ.get('APP_HASH', 'ab1b831edb2bd32905d6572ce621f678')# Telgram App hash  
OWNER_ID = os.environ.get('OWNER_ID', 5514985164)
MONGO_DB = os.environ.get("MONGO_DB", 'mongodb+srv://izumi:None@utahimesexxy.h6jsjbr.mongodb.net/?retryWrites=true&w=majority') #MONGO DB FOR ANIME DATA
FILES_CHANNEL = os.environ.get("FILES_CHANNEL", -1001564797673)
BOT_NAME = os.environ.get('BOT_NAME', 'ongoing vro')
#<---------------Connecting-------------->
if BOT_TOKEN is not None:
    try:
        encoder  = Client('AutoEncoder', api_id=API_ID, api_hash=APP_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
        LOG.info('❤️ Bot Connected Created By Github @soheru || Telegram @sohailkhan_indianime ')
    except Exception as e:
        LOG.warn(f'😞 Error While Connecting To Bot\nCheck Errors: {e}')
        sys.exit()       
