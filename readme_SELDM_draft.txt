Stochastic Empirical Loading Dilution Model, Carter and Wall Creeks, Oregon

Stonewall, A.J., Yates, M.C., and Granato, G.E., 2022, Assessing the Impact of Chloride Deicer Application in the Siskiyou Pass, Oregon: U.S. Geological Survey Scientific Investigations Report 2022-XXXX, XXX p., https://doi.org/xxxx/sirXXXX

An stochastic, empirical model of road crossings in Carter Creek and Wall Creek watersheds in the Siskiyou Pass of southern Oregon. The model is used to estimate the probability of exceeding water quality standards at road crossings, and to estimate constituent loading downstream of the crossings.

Directory structure:

"Contents"
Contains the readme.txt file.

“ModelInput”
Contains the SELDM model project (SELDMv1.2.0-Syskiyou_Chloride.accdb)
This MicroSoft Access database contains all input files used in for SELDM simulations, and the model itself.
Contains a text file (ModelInputs_readme.txt) that describes where the inputs are located in the SELDM model MS Access database.  

“ModelOutput”
Contains 15 subfolders, one for each model simulation scenario. See Table 3 in Stonewall and others (2022) for details of each model scenario. Within each subfolder is another folder, which is labeled with the date of the simulation. Each of these folders contains a subfolder with the model run name (usually "Run001").  Within each of these folders is the following list of output files:
  XXX-Annual.txt -- Annual Highway Runoff Loads
  XXX-DF.txt -- Dilution Factors
  XXX-DQ.txt -- Downstream Water Quality
  XXX-HQ.txt -- Highway Runoff Quality
  XXXOut.txt -- Full description of all output files
  XXX-PE.txt -- Precipitation Events
  XXX-PS.txt -- Prestorm Streamflow
  XXX-SF.txt -- Stormflows
  XXX-UQ.txt -- Upstream Water Quality
Where 'XXX' is the name of the model run (for example "CarterLvl1-Annual.txt").

“SourceCodeandExecutables”
The file "readme.txt" contains the path to the ScienceBase publication for SELDM, which houses the model source code and instructions for installing SELDM. 

SELDM was run using a Windows 10 platform, using the MircoSoft Office 365 version of Access. 

Instructions for running model:
1. Open the database in MicroSoft Access. 
2. From the home screen, hit the "proceed" button.
3. From the "Analyst Identification" module, hit the "Enter New Analyst" button, and input information of analyst.
4. Click "proceed"
5. From the "Project Identification" module, click "proceed"
6. Select the analysis of choice using the dropdown menu.
7. Click "proceed" several times until you reach the run module (labeled "Stochastic Empirical Loading and Dilution Model"). Do not edit any information in the other modules. If changes are needed, a new analysis should be created in step 5.
8. Click the "Run SELDM" button.
9. Note where files are created on the "Output File Locations" tab.