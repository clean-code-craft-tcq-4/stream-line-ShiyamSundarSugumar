import sys

def Read_from_console():
    #i=0
    StreamLinedata = []
    StreamLinedata = sys.stdin.readlines()
    dataIndexOfTemperature = (StreamLinedata).index('Temperature,SOC\n')
    dataIndexOfTestSuccess = (StreamLinedata).index('Test Run Successful.\n')
    '''   
    while(i<(dataIndexOfTestSuccess-1)):
        StreamLinedata = []
        StreamLinedata.append(input())
        i+=1
    '''
    FormattedStreamLinedata = StreamLinedata[(dataIndexOfTemperature+1):(dataIndexOfTestSuccess-1)]   
    return FormattedStreamLinedata
    

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

   
