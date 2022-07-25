'''Svb Airport'''


from datetime import datetime, timedelta


def main():
    '''This is main function'''

    input()
    destination = input()
    depart_time = input()

    converted_time = datetime.strptime(depart_time, '%I:%M %p')
    destination_airport_code = destination[destination.find("(") + 1:destination.find(")")].upper()

    if destination_airport_code == 'SYD':
        converted_time += timedelta(hours=12)
    elif destination_airport_code == 'SGN':
        converted_time += timedelta(minutes=110)
    elif destination_airport_code == 'ATL':
        converted_time += timedelta(hours=9, minutes=55)
    elif destination_airport_code == 'YVR':
        converted_time += timedelta(hours=2, minutes=20)
    elif destination_airport_code == 'KTM':
        converted_time += timedelta(hours=11, minutes=45)

    print('BKK - %s' % destination_airport_code)
    print(converted_time.strftime('%I:%M %p'))


main()
