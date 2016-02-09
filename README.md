## Smart Grid, Smart City Visualizer


As more household appliances become part of the Internet of Things (IoT), it will be valuable for producers and 
consumers to determine which items to upgrade first. Intelligent control of high energy consumption devices can become important tools for the 'Smart Grid'. For example, a user may tell their washing machine to run "some time today". The washing machine will then communicate with the utility to determine a time to run that will put the least strain on the electric grid. Common sense suggests smart control of dishwashers, 
washing machines and driers first, but is this really the best place to start?
 
From October 2010 through February 2014, the Australian government funded the [*Smart Grid, Smart City*]
(http://www.industry.gov.au/ENERGY/PROGRAMMES/SMARTGRIDSMARTCITY/Pages/default.aspx) (SGSC) project. As part of this project, 
800+ households installed Home Area Network (HAN) plugs that monitored the energy consumption of various household items
 over 30-minute intervals. This is the first publically available dataset that provides this information. 
  
This GitHub project aims to provide visualization tools and data analysis to help interested parties see what 
household products are on at what times.
 
Future work using the SGSC dataset may also include:

-   How much energy was saved during peak energy events when the utility offered rebates for households to consume less 
energy during those hours.
-   Following above, how did the consumers responses to rebates changes over the 3+ years that the dataset covers.

### Implimentation

SGSC provides a free [CKAN Data API](http://docs.ckan.org/en/latest/maintaining/datastore.html) which will be used to
query the energy consumption data. This project will create a Python app hosted on [Heroku](https://www.heroku.com/) 
that provides a user-friendly way to produce graphs of data usage of household item based on time, location, and grid 
events. [Bokeh](http://bokeh.pydata.org/en/latest/) will be used to generate interactive plots, and [Flask](http://flask.pocoo.org/) will be used to create the web framework.
 
 Future iterations will also include filtering consumption trends based on weather data provided by [forecast.io](http://forecast.io/).
  
 