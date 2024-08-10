url_input = str(input("Scribd URL: "))

# Sample URL: https://www.scribd.com/document/441480158/User-Manual-for-LED-Digital-Clock

document_id = url_input.split("/")[4]

url_output = f"https://www.scribd.com/embeds/{document_id}/content?start_page=1&view_mode=scroll"

print(url_output)

