using System;
using System.Collections.Generic;
using System.Text;
using Xunit;


namespace Streamline_Sender_TestCase
{
    public class UnitTest
    {
        List<IUtilities> utilities = new List<IUtilities>
            {
                new Sender { fileName = "SensorParameterReadings.csv" },
                new Sender { fileName = "TestFile.csv" },
                new Sender { fileName = "NoFile.csv" },

            };


        [Fact]
        public void CheckFileExists()
        {
            Assert.True(utilities[0].CheckIfFileExists());
            Assert.True(utilities[1].CheckIfFileExists());
            Assert.False(utilities[2].CheckIfFileExists());
        }

        [Fact]
        public void GetDataFromCSVFile()
        {

            var tupleList = new List<(string, string)>
            {
                ("Temperature", "SOC"), ("20", "20"), ("25", "30"), ("30", "40"), ("35", "50"), ("40", "60"), ("45", "70")
            };


            var data = utilities[1].GetSensorReadings();

            for(int i = 0; i < data.Item1.Count; i++)
            {
                
                Assert.Equal(tupleList[i].Item1, data.Item1[i]);
            }

            for (int i = 0; i < data.Item2.Count; i++)
            {
                
                Assert.Equal(tupleList[i].Item2, data.Item2[i]);
            }


        }

        [Fact]
        public void Send_Data_To_Receiver()
        {
            List<string> Temperature = new List<string>();
            List<string> StateOfCharge = new List<string>();
            
            var data = utilities[0].GetSensorReadings();
            
            
            foreach (var i in (data.Item1)) Temperature.Add(i);
            foreach (var i in (data.Item2)) StateOfCharge.Add(i);

            for (int k=0 ; k<data.Item1.Count ; k++)
            {
                string BMS_Sender = $"[{Temperature[k]},{StateOfCharge[k]}]";
                Console.WriteLine(BMS_Sender);
            }
                     
            
        }
    }
}
