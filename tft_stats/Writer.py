import xlrd
import os


book = xlrd.open_workbook("/Users/yuutajorand/PycharmProjects/DeepLearningBot/tft_stats/STATS_TFT.xlsx")
sh = book.sheet_by_index(0)

name = ""
filename = "_stats_lvl_"
lvl = 1
extension = ".txt"




for column in range(2, 58):

    lvl = 1

    name = sh.cell_value(3, column)
    print(name)
    StatSheet = open(name + filename + str(lvl) + extension, "w")
    StatSheet.write(name)
        
    while lvl < 4:
    
        for row in range(3 + lvl, 28, 3):

            value = sh.cell_value(row, column)
            print(value)
            StatSheet.write(value)
            
            StatSheet.close
            StatSheet = open(name + filename + str(lvl) + extension, "r")
            print(StatSheet.read())

        lvl = lvl + 1

    
        

        

        

        


