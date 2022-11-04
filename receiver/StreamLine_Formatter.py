import sys

def Read_from_console():
    i=0
    data = []
    data = sys.stdin.readlines()
    print(data)
    '''
    while(i<77):
        StreamLinedata.append(input())
        i+=1
    FormattedStreamLinedata = StreamLinedata[27:77]
    '''
    dataIndexOfTemperature = (data).index('Temperature,SOC\n')
    dataIndexOfTestSuccess = (data).index('Test Run Successful\n')
    FormattedStreamLinedata = data[dataIndexOfTemperature:dataIndexOfTestSuccess-1]
    print(FormattedStreamLinedata)
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

   
