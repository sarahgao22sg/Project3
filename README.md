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



### Project Description/Outline: 

    • Analysis of invasive species zebra mussel and Greenhouse frog. Invasive species cause ecological, environmental, and economic damage.
      The impacts of invasive species on our natural ecosystems and economy cost billions of dollars each year.
      
    • Analysis the spread of zebra mussle and Greenhouse frog in the United States. 

### Research Questions and Answers:

 **Make an Assumption–** 
 
    1. How have the different species dispersion changed over time?

        The Green house frog had a very linear growth over nearly 150 years, while the Zebra Mussel had an unprecedented geomotric growth and spread over about 30 years.
    
    2. Do the species densities seem to follow any regular patterns or cycles?

        It is hard to answer precisely as the data is more about "sightings" than any true scientific measure.
    
    3. How has the economy been impacted from the zebra mussel species?

        The Economy has been impacted immensely as during the early spread from 1990 to 2000 $8.8 billion was spent in the power production industry alone.

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

    By extrapolation we determined that California and Utah will soon contain the same types of numbers of Zebra Mussels that currently inhabit much of the Upper Midwest.

    Our Machine Learning model requires more accurate collection methods of Zebra Mussel Larvae, before the ML models can help researchers focus their resources on specific Temperatures, Locations, and methodologies. There are simply far too many null larvae points to train an accurate ML Model.


