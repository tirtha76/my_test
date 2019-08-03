import time

bike_tag_database = {'1234':'KA 27 E 4523','4567':'KA 53 SS 1026','7894':'MH 22 FT 4503','1236':'AP 12 JK 4041'}

today_log = []


def ORPAK_IOCL():
    pump_side_reader = input("\nScanning Tag Number:  ")
    print("\nTag number is verifying in server\n")
    time.sleep(4)
    try:
        if pump_side_reader in bike_tag_database:
            print("Reader OK")
            time.sleep(2)
            print("Fuel is Supplying to Vehicle Number:{}\n".format(bike_tag_database[pump_side_reader]))
            today_log.append(pump_side_reader)
        else:
            today_log.append(pump_side_reader)
            print("Invalid Tag or Bike\n")
    except:
        print("server error\n")

def Today_log():
    print("Fuel Supplied Today\n")
    for item in today_log:
        if item in bike_tag_database:
            print("Vehical Number:{}   Tag Number:{}".format(bike_tag_database[item],item))
        else:
            print("At this moment Invalid Tag found, Invalid Tag Number: {}".format(item))
    print("Thank You")

i = 0
while i<1:
    c = input("Want to fill fuel ('1' for 'YES', else any for 'NO') :    ")
    if c == '1':
        ORPAK_IOCL()
    else:
        print("OK\n")
        break
    
