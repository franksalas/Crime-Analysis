
## Datasets

### Crime data
- [x] [Houston Police Department Crime Statistics](http://www.houstontx.gov/police/cs/crime-stats-archives.htm)
	- years: 2009 - 2016
	- format: Access or Excel

### Sports Team schedule & scores

- [x] [sportradar.us](https://developer.sportradar.com/)
-  Multiple sports scores + other data.
-  offers a free 90 day data trial (API) for new users.
- format: JSON

	-  [x] Houston Texans game schedule
		- 17 years of every NFL score from sportradar.us
		- 2001 - 2017
		- date_time|home|h_score|away|a_score|winner
	-  [x] Houston Astros game schedule
		- 2008 - 2017 Houston Astros regular season
		- site
	-  [ ] Houston Rockets game schedule
	-  [x] University of Houston football schedule
		- 2008 - 2017 schedule
	-  [x] Rice University football schelude
		- 2008 - 2017 schedule
	-  [x] Texas Southern University football schedule
		- 2008 - 2017 schedule


## Installation

### Create enviroment from the yaml file

1. create the enviroment from teh `enviroment.yml` file

```bash
conda env create -f environment.yml
```

2. activate the new enviroment

- windows : `activate sbc`
- osx & linux : `source activate sbc`