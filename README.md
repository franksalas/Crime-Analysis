
## Datasets

### Crime data
- [x] [Houston Police Department Crime Statistics](http://www.houstontx.gov/police/cs/crime-stats-archives.htm)
	- years: 2010 - 2017
	- format: Access or Excel

### Sports Team schedule & scores

- [x] [sportradar.us](https://developer.sportradar.com/)
-  Multiple sports scores + other data.
-  offers a free 90 day data trial (API) for new users.
- format: JSON
- scores from 2010-2017
	-  [x] Houston Texans game schedule
	-  [x] Houston Astros regular/post season
	-  [x] Houston Rockets regular/post season
	-  [x] University of Houston football regular/post season
	-  [x] Rice University football schelude



## Installation

### Create enviroment from the yaml file

1. create the enviroment from teh `enviroment.yml` file

```bash
conda env create -f environment.yml
```

2. activate the new enviroment

- windows : `activate sbc`
- osx & linux : `source activate sbc`