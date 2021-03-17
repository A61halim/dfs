from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from notify import notification
from server import server
from tabulate import tabulate
from dictionnary import server_list
from loop import loop
import time

ser = [['Agride',1],
['Atcham',2],
['Boune',3],
['Brumen',4],
['Crail',5],
['Echo',6],
['Eratz',7],
['Furye',8],
['Galgarion',9],
['Henual',10],
['Ilyzaelle',11],
['Jahash',12],
['Julith',13],
['Meriana',14],
['Merkator',15],
['Nidas',16],
['Ombre(Shadow)',17], 
['Oto Mustam',18],
['Pandore',19],
['Rubilax',20],
['Temporis I ',21],
['Temporis II',22] ,
['Thanatena',23],
['USH',24]]
print(tabulate(ser))
s = int(input('Enter the number for your Server: '))



loop.boucle(server_list[ser[s-1][0]])
