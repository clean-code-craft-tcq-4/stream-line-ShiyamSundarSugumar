import sys
import ast
import pandas as pd
import re

def StreamLineformat_console_pipeline():
    i=0
    data_1 = []
    while(i<77):
        data_1.append(input())
        i+=1

    print(data_1)
    print(" Summa \n ")
    data_2 = data_1[27:77]
    i=0
    Temp_data = []
    SOC_data = []
    while(i<50):
        temp = data_2[i].split(",")
        StreamLineReceiver_temperature_list.append(int(temp[0]))
        StreamLineReceiver_soc_list.append(int(temp[1]))
        i+=1    
   
    return [StreamLineReceiver_temperature_list,StreamLineReceiver_soc_list]

    else:
        return None
