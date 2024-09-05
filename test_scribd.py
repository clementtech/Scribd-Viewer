# Code to test scribd_bot.py

import scribd_bot

def test_link():
    assert bypass("https://www.scribd.com/document/441480158/User-Manual-for-LED-Digital-Clock") == "https://www.scribd.com/embeds/441480158/content?start_page=1&view_mode=scroll"