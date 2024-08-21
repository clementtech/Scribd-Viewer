# Sample URL: https://www.scribd.com/document/441480158/User-Manual-for-LED-Digital-Clock

# Creates a loop to repeat asking user if input is not a valid document link
while True:

    # If it's a valid document link
    try:

        # Receive input from the user in string format
        url_input = str(input("Scribd URL: "))

        # Process the document link and strip out the document id
        document_id = url_input.split("/")[4]

    # If user input not a valid Scribd document id
    except IndexError:

        # Tells the user to input a valid document link
        print("Please enter a valid Scribd Document URL")

    # If the user input the valid document link
    else:

        # New link where paywall is removed
        url_output = f"Enjoy: https://www.scribd.com/embeds/{document_id}/content?start_page=1&view_mode=scroll"

        # Stop the loop
        break


# Print out the new link where paywall is removed
print(url_output)
