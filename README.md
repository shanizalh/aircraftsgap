# Aircraft sgap

This is a simple source code used to process aircraft sgap (structure gap) data in my company.

In SAP system, structure gap is a placeholder for a missing part in the actual configuration of a technical object. In my case, the technical object is single aircraft registration. So, with structure gap, we could know what components of the aircraft configuration is currently missing.

The code has been slightly modified and 1 additional file has been omitted as it consist of confidential aircraft maintenance data.

Files in this repo:
1. 8 example source files (output from SAP sgap system for each aircraft registration)
2. raw python script file
3. jupyter notebook file to see the data frame
4. 1 example output file

How to use:

Put all the files in one directory, and run the python/jupyter script. The output file will be generated as .xlsx file.

Resulted Data Frame:
Fleet | Floc | Message | type (R/A/G) | Error number | Functional identifier (FID) | Message text | Material | Sequence

Feel free to download, modify, or use for your own work. Or you can raise new issue or make pull requests.
Thank you.