
import StreamLine_Formatter

# returns minimum value from list of StreamLine data parameter
def StreamLineReceiver_min(StreamLine_data):
    if len(StreamLine_data) !=0:
        return round(min(StreamLine_data),3)
    return "Data not available"

# returns maximum value from list of StreamLine data parameter
def StreamLineReceiver_max(StreamLine_data):
    if len(StreamLine_data) != 0:
        return round(max(StreamLine_data), 3)
    return "Data not available"


# report the statistics of StreamLine data received from sender
def displayOutput(StreamLine_data):
    if(StreamLine_data!=None):
        StreamLine_temperature_list = StreamLine_data[0]
        StreamLine_soc_list = StreamLine_data[1]

        print('Max Temperature:', StreamLineReceiver_max(StreamLine_temperature_list))
        print('Min Temperature:', StreamLineReceiver_min(StreamLine_temperature_list))
        print('Moving average of last five values of temperature:', StreamLineReceiver_moving_average_last_5(StreamLine_temperature_list))

        print('Max SOC:', StreamLineReceiver_max(StreamLine_soc_list))
        print('Min SOC:', StreamLineReceiver_min(StreamLine_soc_list))
        print('Moving average of last five values of SOC:', StreamLineReceiver_moving_average_last_5(StreamLine_soc_list))
    return 'Success'

# returns moving average of last 5 values in bms parameter list
def StreamLineReceiver_moving_average_last_5(StreamLine_data):
    length = len(StreamLine_data)
    if length >= 5:
        moving_average = round((sum(StreamLine_data[-5:])/5),3)
        return moving_average
    return "Data Insufficent"

def Pipeline_Data_Check():
    displayOutput(StreamLine_Formatter.StreamLineformat_console_pipeline(StreamLine_Formatter.Read_from_console()))
    
    
if __name__ == '__main__':
    Pipeline_Data_Check()
