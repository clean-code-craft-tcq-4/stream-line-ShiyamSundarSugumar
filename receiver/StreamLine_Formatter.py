import sys
import pandas as pd

def Read_from_console():
    i=0
    data_1 = []
    while(i<77):
        data_1.append(input())
        i+=1
    data_2 = data_1[27:77]
    return data_2
    

def StreamLineformat_console_pipeline(data):
    i=0
    StreamLineReceiver_temperature_list = []
    StreamLineReceiver_soc_list = []
    while(i<len(data)):
        temp = data[i].split(",")
        StreamLineReceiver_temperature_list.append(int(temp[0]))
        StreamLineReceiver_soc_list.append(int(temp[1]))
        i+=1    
    return [StreamLineReceiver_temperature_list,StreamLineReceiver_soc_list]

    
