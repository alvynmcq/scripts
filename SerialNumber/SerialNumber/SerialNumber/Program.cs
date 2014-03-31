using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Management;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            // Generate a sequence of integers from 1 to 147  
            // this represents the station number
            IEnumerable<int> machine_number = Enumerable.Range(1, 147);
            // List to write station name strings into
            List<string> workstation_names = new List<string>();
            // Write station names to list
            foreach (int num in machine_number)
            {
                if (num < 10)
                    workstation_names.Add("3420094-STN00" + num);
                else if (num < 100)
                    workstation_names.Add("3420094-STN0" + num);
                else
                    workstation_names.Add("3240094-STN" + num);
            }
            // WMI query machines for details
            foreach (string names in workstation_names)
            {
                try
                {
                    ManagementScope scope = new ManagementScope(@"\\" + names + @"\root\cimv2");
                    scope.Connect();

                    ObjectQuery details = new ObjectQuery("SELECT * FROM Win32_Bios");

                    ManagementObjectSearcher searcher = new ManagementObjectSearcher(scope, details);
                    ManagementObjectCollection queryCollection = searcher.Get();

                    foreach (ManagementObject stuff in queryCollection)
                    {
                        Console.WriteLine("-------------------");
                        Console.WriteLine("Details");
                        Console.WriteLine("-------------------");
                        Console.WriteLine("StationNumber: {0}", names);
                        Console.WriteLine("SerialNumber: {0}", stuff["SerialNumber"]);
                        Console.WriteLine("-------------------");
                    }
                }
                catch
                {
                    Console.WriteLine("Machine not responding.");
                }
            }
        }
    }
}
