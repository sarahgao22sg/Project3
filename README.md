# Invasive Species 

## Project 3 Group 10: Josh Bond, Nicole Pipkins, and Yushan Sarah Gao

**Link to GitHub Repository:** https://github.com/sarahgao22sg/Project3

### Repository Structure and Navigation

1. Resources folder contains initial download CSV's

2. Data folder contains the DataFrames merged and cleaned for Data Visualization

3. Images folder contains various types of images

4. Analysis folder contains the .ipynb files for transforming data and ML

5. teplates folder contains the html webpages for displaying the visuals

6. **app.py** is the python file that runs our **Flask** Server.



 **Data Puller**- Queries for BLS, TLM, and COVID-19 Data
     
    CSV exports to Resources Folder
        * 

 **BLS_DFs_Plts**- BLS data merging and analysis
    
    Imports
        * 
    
    Exports
        * 
       

 **Statistical Analysis of Covid Data**
    
    Imports
        * 
       
    
    Exports
        * 

 
 **Texas vs New York in Positive Covid-19 Testing by Month bar chart**
    
    Imports
        * 
    
    Exports 
        * 
   
**ProjectDataJanette**
    
    Imports
        * 


    Exports
        * 
        
      
 **Group4 Project 1Notebook_geomap**
    
    Imports
        * 


    Exports
        *     
 
    
 **Annual % Change By Industry During Covid-19 bar chart #1**

    Imports 
        * 

    Exports
        * 

### Project Description/Outline: 

    • Analysis of Job Turnover and Separation because of COVID-19 by using Texas Market Data, Covid Tracking Data and Bureau of Labor Statistics.

    • United States and Texas Unemployment Rate Comparison by providing geospatial visualizations specifically delta change per County between July 2019 and July 2020 • Texas Labor Market Analysis for Percent Women and Men COVID Positive Tests with a Line Graph over April 2020 to August 2020 • Total claims for Houston between Jan 2019 to July 2020 with a Line Graph

    • Percent of Unemployment Rate by Men, Women and Teenagers with a Line Graph • Bar graph comparison of Positive Tests Per Month for Texas and New York • Comparing Industry by Industry Annual % Change of Unemployment Rate via Bar Graph • Statistical Analysis

### Research Questions and Answers:

 **Make an Assumption–** 
 
    1. How have the different species dispersion changed over time?
    
    2. Do the species densities seem to follow any regular patterns or cycles?
    
    3. How has the economy been impacted from the zebra mussel species?

 **Data Sets to be Used:** 

     *   https://dec.vermont.gov/watershed/lakes-ponds/aquatic-invasives/monitoring/zebra-mussels
         USED FOR MACHINE LEARNING MODEL - zebra mussel larvae collection data: collecting_zebra.csv

     *  https://nas.er.usgs.gov/queries/factsheet.aspx?speciesID=5
        JOINED WITH OTHER NAS DATASET FOR VIZ - mussel sighting data: Exotic – Zebra Mussels.csv

     *  https://nas.er.usgs.gov/queries/FactSheet.aspx?speciesID=61
        JOINED WITH OTHER NAS DATASET FOR VIZ - frog sighting data: Exotic – Greenhouse Frog.csv 

     * https://www.epa.gov/sites/production/files/2014-12/documents/economic_impacts_of_aquatic_invasive_species.pdf
       USED FOR IMPACT - Economic Impacts of Zebra Mussels: zebra_mussel_economic_impact_facts.csv
 

### Conclusions:

    For the months of May through August their is a very strong correlation between between COVID 19 cases and Texas County unemployment data. May being the earliest due to volume of testing being statistically relevant, and August being the latest month for which we had unemployment data.

    We assume that positive COVID 19 cases will go down as parents that were laid off stayed home, to determine would require finding the derivative of the slope over time. From general observation this is the case leading to the conclusion that the less people unemployed led to a lower change in decreasing % positives over time.

    There were more women suffered greater % job losses than men,
    however, teens 16-19 were the highest affected age group. This was the case for both years, leading to the conclusion that the normal state of unemployment spreads from high to low are teens, adult women, adult men.


    There were examples of unemployment % increases, decreases, and stagnation. I would conclude that the effect of unemployment percentage pre and post covid is mostly in magnitude which could be determined by year over comparisons.

    Couriers and Messengers industry has positive growth and support activities for Mining (suppliers, transportation and materials)
