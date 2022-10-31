import unittest
import StreamLine_Reporter
from StreamLine_Formatter import StreamLineformat_console_pipeline

class test_StreamLine_receiver(unittest.TestCase):
    
    #test StreamLineReceiver_min function
    def test_StreamLineReceiver_min_calculator(self):
        StreamLineReceiver_min = StreamLine_Reporter.StreamLineReceiver_min([10,12,14,15,18])
        self.assertTrue(StreamLineReceiver_min is not None)
        self.assertTrue(StreamLineReceiver_min == 10)
        StreamLineReceiver_min = StreamLine_Reporter.StreamLineReceiver_min([])
        self.assertTrue(StreamLineReceiver_min == 'Data not available')
        self.assertFalse(StreamLineReceiver_min == 0.58)
    
    #test StreamLineReceiver_max function
    def test_StreamLineReceiver_max_calculator(self):
        StreamLineReceiver_max = StreamLine_Reporter.StreamLineReceiver_max([10,12,14,15,18])
        self.assertTrue(StreamLineReceiver_max is not None)
        self.assertTrue(StreamLineReceiver_max == 18)
        StreamLineReceiver_max = StreamLine_Reporter.StreamLineReceiver_max([])
        self.assertTrue(StreamLineReceiver_max == 'Data not available')
        self.assertFalse(StreamLineReceiver_max == 0.15)
    
    #test StreamLineReceiver_moving_average_last_5 function
    def test_StreamLineReceiver_moving_avg_calculator(self):
        StreamLineReceiver_moving_average = StreamLine_Reporter.StreamLineReceiver_moving_average_last_5([5,6.5,2,3])
        self.assertTrue(StreamLineReceiver_moving_average == 'Data Insufficent')
        self.assertFalse(StreamLineReceiver_moving_average == 7.5)
        StreamLineReceiver_moving_average = StreamLine_Reporter.StreamLineReceiver_moving_average_last_5([5, 6.5, 2, 3,8,9.5])
        self.assertTrue(StreamLineReceiver_moving_average == 5.8)
        
    # test if StreamLineReceiver statistics report is printed successfully
    def test_StreamLineReceiver_statistics_reporting(self):
        self.assertTrue(StreamLine_Reporter.displayOutput(StreamLineformat_console_pipeline()) == 'Success')


if __name__ == '__main__':
    unittest.main()
