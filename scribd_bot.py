# Sample URL: https://www.scribd.com/document/441480158/User-Manual-for-LED-Digital-Clock
while True:
    try:
        url_input = str(input("Scribd URL: "))

        document_id = url_input.split("/")[4]

    except IndexError:
        print("Please enter a valid Scribd Document URL")

    else:
        url_output = f"Enjoy: https://www.scribd.com/embeds/{document_id}/content?start_page=1&view_mode=scroll"
        break

print(url_output)
