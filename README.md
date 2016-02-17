## Smart Grid, Smart City Visualizer

Household appliances may soon become active players in the smart grid. For example, a user could tell their washing 
machine to run "sometime today". The washing machine would then communicate with the utility to determine the time to 
run that will put the least strain on the electric grid. This will improve the stability of the grid and result in 
greater overall energy efficiency. This project seeks to determine which devices are low hanging fruit in this movement.
 Common sense suggests smart control of dishwashers and washing machines first, but is this really the best place to start? 

From October 2010 through February 2014, the Australian government funded the [*Smart Grid, Smart City*]
(http://www.industry.gov.au/ENERGY/PROGRAMMES/SMARTGRIDSMARTCITY/Pages/default.aspx) (SGSC) project. As part of this 
project, 800+ households installed Home Area Network (HAN) plugs that monitored the energy consumption of various 
household items in 30-minute intervals. 
  
This project seeks to create visualization tools and data analysis to help interested parties see what household products are on at what times.

### Implementation
The SGSC project hosts their data using a [CKAN Data API](http://docs.ckan.org/en/latest/maintaining/datastore.html) which will be used 
to query the energy consumption data. This project will create a Python app hosted on [Heroku](https://www.heroku.com/) 
that provides a user-friendly way to produce graphs showing the usage of household items. 
At a minimum, the filters will include:

-   Device to examine (dishwasher, dryer, etc).
-   Time of day.
-   Month of year.
-   Weather patterns (cloudy, sunny, stormy).
-   Postal code of household.
-   Income of household (low, medium, high).
-   Whether or not the household has a solar array.

[Bokeh](http://bokeh.pydata.org/en/latest/) will be used to generate interactive plots, [Flask](http://flask.pocoo.org/) 
will be used to create the web framework, and [forecast.io](http://forecast.io/) will be used to determine the weather patterns.

### Proof of Concept (pre-beta)
A very basic heroku app is hosted at [https://smartgridsmartcity.herokuapp.com/index](https://smartgridsmartcity.herokuapp.com/index). 
At present, I only list sites that had at least 3 HAN plugs.

### Future Work
Analysis of the HAN devices is just one potential use of the SGSC dataset. Future plans include:

-   During peak consumption events, Australian utilities offered rebates to households if they consumed less energy 
during those hours. How much energy was saved by doing this? 
-   Following above, how did the consumers' response to rebate offers change over the 3+ years that the dataset covers?
-   Machine learning can be used on this dataset to predict household consumption based on weather patterns. 
How much historical data is required to provide accurate estimates?
