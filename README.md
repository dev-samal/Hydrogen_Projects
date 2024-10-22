# HFCs as Sustainable Energy Source
### Hydrogen Fuel Cells (HFCs) are part of many global sustainability programs. HFCs produce no harmful emissions because the only by products are heat and water, greatly reducing the risk of mismanagement and accidents with storing toxic material like battery acid or diesel fuel. 

Today, hydrogen is primarily used in industrial processes, such as rocket fuel, electricity generation, and powering vehicles. In the United States, hydrogen is used for various refinement processes, production of fertilizer and chemicals, production of renewable diesal, etc. Hyrdrogen power is among the many sustainable solutions for large manufacturing corporations of steel or chemical seeking to reduce carbon footprint. Current research in transition of HFCs has shown increased energy efficieny, lower operational costs, and durability in extreme weather environment. 

While HFC's are new and exciting, infrastructure, funding and much time is required before significant transitions are made among the general population of HFC's. This dataset and app simply explores the current interest in hydrogen production via electrolysis, natural gas reforming, etc. The is app reflect that many countries are budgeting and planning to begin there own hyrdrogen production programs to build enviromental sustainability. 

### To view the app go to ### 
https://h2projects.streamlit.app/
____________________________________________________________________________________________________________
**Recreate the app**
1. Download all items from folder
2. Save the dataset (H2Projects.csv) in the same folder and .py file
3. Open H2Project.py in Visual Studio Code
4. Run H2Projects.py with command * *streamlit run H2.Projects.py* *
____________________________________________________________________________________________________________
**Data Sources**
- https://www.iea.org/data-and-statistics/data-product/hydrogen-production-and-infrastructure-projects-database
____________________________________________________________________________________________________________
**Background Reading**
- https://www.eia.gov/energyexplained/hydrogen/use-of-hydrogen.php
- https://www.energy.gov/eere/fuelcells/hydrogen-production
- https://www.iea.org/reports/global-hydrogen-review-2023
____________________________________________________________________________________________________________
**Data Prep**

The dataset is comprised of statistics from news releases, announcement, and articles. The data is updated at least once a year. Currently the app uses data as of 2022. The dataset signifies if a project implements carbon capture with "CCUS". To visualize the application of carbon capture implementation, I added a 'carbon capture' column to identify if a project plans carbon capture or not; 1 means yes, blank means no. I converted country abbreviations to full country names to bring clarity to the locations of planned projects. Country name is used to join a longitude and latitude table for creation of maps.
____________________________________________________________________________________________________________
**Future Plan**

Future updates to this app would include refreshing date with IEA's newest information. Since the visuals and dashboard informs on global interest, and initial research and development of hydrogen projects, next steps to improve the app include focusing in on one end user industry. The goal would be to show cause and effect, if any, of the appllication of H2 fuel cells on various industries. Another route of expansion would be an cost analysis of implementing these projects by country and seeing if the cost is worth the reduction in carbon emissions.

