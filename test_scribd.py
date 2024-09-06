# Code to test scribd_bot.py

# Import the bypass feature from the scribd_bot program
from scribd_bot import bypass

# Create a test to checks if the link sucessfully converted into a non paylink document
def test_link():
    assert bypass("https://www.scribd.com/document/441480158/User-Manual-for-LED-Digital-Clock") == "https://www.scribd.com/embeds/441480158/content?start_page=1&view_mode=scroll"
