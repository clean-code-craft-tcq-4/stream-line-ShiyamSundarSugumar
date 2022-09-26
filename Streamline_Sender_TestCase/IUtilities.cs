using System;
using System.Collections.Generic;
using System.Text;

namespace Streamline_Sender_TestCase
{
    interface IUtilities
    {
        public string fileName { get; set; }
        Tuple<List<string>, List<string>> GetSensorReadings();

        public bool CheckIfFileExists();
        
    }
}
