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
    data_2 = data_1[27:76]
    i=0
    Temp_data = []
    SOC_data = []
    while(i<50):
        temp = data_2[i].split(",")
        Temp_data.append(int(temp[0]))
        SOC_data.append(int(temp[1]))
        i+=1    
        
        
    print(Temp_data)
    print(SOC_data)
      
    
    
    data = sys.stdin.readlines()
    input_data = ''
    #print(data)
    if(data != []):
        def findIndex(data):
            dataIndexOfTemperature = data.index('[Temperature,SOC]\n')
            print(dataIndexOfTemperature)
        IndexOfTemperature = findIndex(data)

        def filterFunc(data):
            if(data == '[Temperature,SOC]\n'):
                return True
            else:
                return False
        Streamdata = filter(filterFunc, data)
        for x in Streamdata:
            print(x)
        #get the streaming data from dotnet console output in the pipeline
        for line in data:
            if '[Temperature,SOC]\n' in line:
                input_data = line

        #convert StreamLine data string to list of dictionaries
        formated_data_stream = ast.literal_eval(input_data)

        #convert the list of dictionaries to a dataframe and return bms parameter lists
        StreamLine_dataframe = pd.DataFrame(formated_data_stream)
        if StreamLine_dataframe.size !=0:
            StreamLineReceiver_temperature_list = StreamLine_dataframe['temperature'].values.tolist()
            StreamLineReceiver_soc_list = StreamLine_dataframe['soc'].values.tolist()
            return [StreamLineReceiver_temperature_list,StreamLineReceiver_soc_list]
    else:
        return None
