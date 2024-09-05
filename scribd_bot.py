# Sample URL: https://www.scribd.com/document/441480158/User-Manual-for-LED-Digital-Clock

def main():
    # Creates a loop to repeat asking user if input is not a valid document link
    while True:

        # If it's a valid document link
        try:

            # Receive input from the user in string format
            print(bypass((str(input("Scribd URL: "))).split("/")[4]))

        # If user input not a valid Scribd document id
        except IndexError:

            # Tells the user to input a valid document link
            print("Please enter a valid Scribd Document URL")

        except EOFError:
            break
        

def bypass(id)
    return f"Enjoy: https://www.scribd.com/embeds/{id}/content?start_page=1&view_mode=scroll"


if __name__ == "__main__":
    main()