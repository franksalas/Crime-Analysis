
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

	-  [ ] Houston Texans game schedule
	-  [ ] Houston Astros game schedule
	-  [ ] Houston Dash game schedule
	-  [ ] Houston Rockets game schedule
	-  [ ] University of Houston football schedule
	-  [ ] Rice University football schelude
	-  [ ] Texas Southern University football schedule


## Installation

### Create enviroment from the yaml file

1. create the enviroment from teh `enviroment.yml` file

```bash
conda env create -f environment.yml
```

2. activate the new enviroment

- windows : `activate sbc`
- osx & linux : `source activate sbc`