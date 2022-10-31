import sys
import ast
import pandas as pd

def StreamLineformat_console_pipeline():
    data = sys.stdin.readlines()
    input_data = ''
    print(data)
    if(data != []):
    
        #get the streaming data from dotnet console output in the pipeline
        for line in data:
            if '[Temperature,SOC]' in line:
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
