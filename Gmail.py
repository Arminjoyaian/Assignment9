#from colorama import Fore, Back
#print(Back.LIGHTRED_EX, "Arminjoya1442@gmail.com", Back.RESET)

#from colorama import Fore, Back
#print(Back.MAGENTA, "Arminjoya1442@gmail.com", Back.RESET)

#import qrcode
#q = qrcode.make("Arminjoya1442@gmail.com")
#q.save(" home the close")

#import segno
#qrcode_2 = segno.make('Arminjoya1442@gmail.com', error='Erorr')
#qrcode_2.save( scale=4, dark='steelblue', data_dark='read')

import segno
_qrcode = segno.make('Arminjoya1442@gmail.com', error='Error')
_qrcode.save( scale=9, dark='blue', data_dark='read')