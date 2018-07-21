## Likelihood of crime around a sports stadium in the city of Houston Texas.

Houston Texas with its 2.4 million residents is the fourth most populous city in the United States, just behind New York, Los Angeles, and Chicago.  As with any large city,  Houston has a rich sporting culture with five professional major league teams and two Division I college athletic programs.  With so many sporting events through the year, what is the likelihood of crime around a sports stadium given event?

Crime happens, given the density of a population there exist [some connection ](https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1745-9125.1979.tb01285.x)of increase of crime.
But how often does it happen around specific areas like a sports arena?
It would be helpful to sports fans if they know the chance that crime around them given the arena.
The local police department could increase/decrease staff given the right information; also city planners could use the information to determine the best way to use a city's land and resources.

The goal of this project is to develop such a predictive model for only crime around stadium arenas in the city of Houston, Texas from the years 2010 to 2017.

The crime data is acquired from [Houston Police Department Crime Statistics](http://www.houstontx.gov/police/cs/crime-stats-archives.htm) site.
Sports dataset is acquired from several locations including [sportradar.us](https://developer.sportradar.com/)
for this study, the data is obtained only from the years 2010 to 2017 inclusive.


```python
# replace extra ' with empty space
crimes['Beat'] = crimes.Beat.str.replace("'", " ")

# strip empty spaces
crimes.Beat = crimes.Beat.str.strip()
```
