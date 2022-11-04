#define __ReadFromCSV


using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using CsvHelper;
using CsvHelper.Configuration;
using System.Globalization;



namespace Streamline_Sender_TestCase
{
    public class Sender: IUtilities
    {
        public struct SensorParameters
        {
            public List<string> Temperature;
            public List<string> StateOfCharge;

        }

        public string fileName { get; set; }

        public Tuple<List<string>,List<string>> GetSensorReadings()
        {
            SensorParameters sensorParameters = new SensorParameters();
            

#if (__ReadFromCSV)

            sensorParameters = GetReadingsFromCSV(fileName);

#else

            sensorParameters = GetReadingsFromRandomArray();
#endif

            return Tuple.Create(sensorParameters.Temperature, sensorParameters.StateOfCharge);
        }

        

        public SensorParameters GetReadingsFromCSV(string filename)
        {
            SensorParameters sensorParameters = new SensorParameters();
            sensorParameters.Temperature = new List<string>();
            sensorParameters.StateOfCharge = new List<string>();

            string line;
            string[] columns;

            using (StreamReader sr = new StreamReader(filename))
            {
                while ((line = sr.ReadLine()) != null)
                {
                    columns = line.Split(',');
                    sensorParameters.Temperature.Add(columns[0]);                  
                    sensorParameters.StateOfCharge.Add(columns[1]);

                }
            }
            return sensorParameters;

        }

        public bool CheckIfFileExists()
        {
            return File.Exists(fileName);
        }

        
        public SensorParameters GetReadingsFromRandomArray()
        {
            SensorParameters sensorParameters = new SensorParameters();
            Random random = new Random();

            sensorParameters.Temperature = new List<string>();
            sensorParameters.StateOfCharge = new List<string>();

            sensorParameters.Temperature.Add("Temperature");
            sensorParameters.StateOfCharge.Add("StateOfCharge");


            int i = 0;
            while (i < 50)
            {
                sensorParameters.Temperature.Add((random.Next(10, 45)).ToString());
                sensorParameters.StateOfCharge.Add((random.Next(20, 80)).ToString());
                i++;
            }

            return sensorParameters;

        }
        

    }
}
