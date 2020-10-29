from datetime import datetime


def openwrite(client, note):
    today = datetime.now()
    date_format = "%m-%d-%Y"
    contact_date = today.strftime(date_format)
    file = open(f'{client}.txt', 'a')
    file.write(f"{contact_date}\n")
    print(client, contact_date)
    file.close()


while True:
    client_name = input("Enter client name or STOP to end\n").lower()
    if client_name == "stop":
        break
    else:
        notes = input("Enter notes:")
        openwrite(client_name, notes)
