import gc

import gspread
import os

import pprint
from oauth2client.service_account import ServiceAccountCredentials

name = ""
filename = "_stats_lvl_"
lvl = 1
extension = ".txt"



scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('STATSTFT-2133776c086c.json', scope)
client = gspread.authorize(creds)

gc = gspread.authorize(creds)
sh = gc.open('STATS TFT')
worksheet = sh.get_worksheet(0)


#sheet = client.open('STATS TFT').sheet1
#tft_stats_scheet = sheet.cell(4, 3).value

#print(tft_stats_scheet)
pp = pprint.PrettyPrinter()

#pp.pprint(tft_stats_scheet)

#cell.row, cell.col

for column in range(3, 58):

    # lvl = 1
    # Health = 0
    # Attack_Damage = 0
    # DPS = 0
    # Attack_Range = 0
    # Attack_Speed = 0
    # Armor = 0
    # Magical_Resistance = 0
    # Rarity_Price = 0

    name = worksheet.cell(4, column).value
    pp.pprint(str(name))
    StatSheet = open(str(name) + filename + str(lvl) + str(extension), "w")
    StatSheet.write(str(name))

    while lvl < 4:

        for row in range((3 + lvl), 28, 3):
           # value = worksheet.get_all_values()  # this is the problem
            #value = worksheet.row_values(3 + lvl)

            Health = worksheet.cell( 4 + lvl , row).value
            Attack_Damage = worksheet.cell(7 + lvl,row).value
            DPS = worksheet.cell(10 + lvl, row).value
            Attack_Range = worksheet.cell(13 + lvl, row).value
            Attack_Speed = worksheet.cell(16 + lvl, row).value
            Armor = worksheet.cell(19 + lvl, row).value
            Magical_Resistance = worksheet.cell(22 + lvl, row).value
            Rarity_Price = worksheet.cell(25 + lvl, row).value

            value = (Health +'\n'+ Attack_Damage +'\n'+ DPS + Attack_Range +'\n'+ Attack_Speed +'\n'+ Armor +'\n'+ Magical_Resistance +'\n'+ Rarity_Price)
            print(type(value))

            #fullStr = '_'.join([str(elem) for elem in value ])
            #print(type(fullStr))
            StatSheet = open(str(name) + filename + str(lvl) + str(extension), "w")
            StatSheet.write(value)


            StatSheet.close
            StatSheet = open(str(name) + filename + str(lvl) + str(extension), "r")
            print(StatSheet.read())

        lvl = lvl + 1
