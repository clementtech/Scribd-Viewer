# Code to test scribd_bot.py

from scribd_bot import bypass

def test_link():
    assert bypass("https://www.scribd.com/document/441480158/User-Manual-for-LED-Digital-Clock") == "Enjoy: https://www.scribd.com/embeds/441480158/content?start_page=1&view_mode=scroll"
