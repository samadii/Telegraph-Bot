import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_OWNER = int(os.environ["BOT_OWNER"])
DATABASE_URL = os.environ["DATABASE_URL"]

# optional
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL")

# optional (set to Anything to enable the force subscribing)
F_SUB = os.environ.get('F_SUB')

# optional (only for enable the exporting webpages to Telegraph function)
TELEGRAPH_TOKEN = os.environ.get('TELEGRAPH_TOKEN')
