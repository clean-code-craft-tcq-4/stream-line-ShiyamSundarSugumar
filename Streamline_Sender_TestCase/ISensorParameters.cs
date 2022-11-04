using System;
using System.Collections.Generic;
using System.Text;

namespace Streamline_Sender_TestCase
{
    interface ISensorParameters
    {
        protected List<int> Temperature { get; set; }
        protected List<int> StateOfCharge { get; set; }

        public void ISensorParameters()
        {
            Temperature = new List<int>();
            StateOfCharge = new List<int>();
        }
    }
}
