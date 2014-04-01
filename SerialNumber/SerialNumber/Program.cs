using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Management;
using System.IO;
using CultureInfo;

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
            // Write station names to list, define prefixes based on station number
            foreach (int num in machine_number)
            {
                if (num < 10)
                    workstation_names.Add("3420094-STN00" + num);
                else if (num < 100)
                    workstation_names.Add("3420094-STN0" + num);
                else if (num > 100)
                    workstation_names.Add("3420094-STN" + num);
            }
            // WMI query machines for details
            foreach (string names in workstation_names)
            {
                try
                {
                    ManagementScope scope = new ManagementScope(@"\\" + names + @"\root\cimv2"); // Set station names to connect to
                    scope.Connect();

                    ObjectQuery details = new ObjectQuery("SELECT * FROM Win32_Bios");          // Get all information from Win32_Bios
                    ObjectQuery boottime = new ObjectQuery("SELECT * FROM Win32_OperatingSystem"); //Get all information from Win32_OperatingSystem

                    ManagementObjectSearcher boot = new ManagementObjectSearcher(scope, boottime); //Search for Win32_OperatingSystem information
                    ManagementObjectSearcher searcher = new ManagementObjectSearcher(scope, details); //Search station for Win32_Bios information
                    ManagementObjectCollection queryCollection = searcher.Get();
                    ManagementObjectCollection osCollection = boot.Get();

                    foreach (ManagementObject gumf in osCollection)
                    {
                        CultureInfo culture = new CultureInfo("pt-BR"); 
                        Console.WriteLine("-----------------------------------");
                        Console.WriteLine("Win32_OperatingSystem instance");
                        Console.WriteLine("-----------------------------------");
                        Console.WriteLine("LastBootUpTime: {0}", gumf["LastBootUpTime"].ToString("d", culture));
                    }

                    // Write station number and serial number to console
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
                
                // Write machine not responding if workstation does not respond to request
                catch
                {
                    Console.WriteLine("Machine not responding: " + names);
                }
            }
        }
    }
}
