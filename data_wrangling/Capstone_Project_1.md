# Project: Capstone Project 1 - Data Wrangling

# Datasets

## Crime data
- Houston Police Department Crime Statistics
	- [years: 2010 - 2017](http://www.houstontx.gov/police/cs/crime-stats-archives.htm)
### Sports results

- Rice University Football
    - [2010 - 2017 results](https://www.sports-reference.com/cfb/schools/rice/2017-schedule.html)
- University of Houston Football
    - [2010 - 2017 results](https://www.sports-reference.com/cfb/schools/houston/2017-schedule.html)
- Texas Souther University Football
    - [2010 - 2017 results](http://www.espn.com/college-football/team/schedule/_/id/2640/year/2017)
- Houston Dynamo Soccer
    - [2000 - 2017](https://github.com/jokecamp/FootballData)
- Houston Rockets
    - [2008-2017 reg & post results](https://www.basketball-reference.com/teams/HOU/2017_games.html)
- Houston Astros
    - [2008 - 2017 reg results](https://www.baseball-reference.com/teams/HOU/2018-schedule-scores.shtml)
- Houston Texans
    - [2008 - 2017 reg results](https://developer.sportradar.com/)
    


# Cleaning process


## Problem:
Some values on a column have extra white spaces.


```python
df17['Offense Type'].unique()

array(['Burglary', 'Theft', 'Robbery', 'Auto Theft', 'Aggravated Assault',
       'Rape', 'Murder', 'AutoTheft', 1, 'Burglary                 ',
       'Robbery                  ', 'Theft                    ',
       'AutoTheft                ', 'Aggravated Assault       ',
       'Rape                     ', 'Murder                   '],
      dtype=object)
```
## Solution:
Call the [pandas.Series.str.strip](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.str.strip.html) to remove any white spaces


```python
df17['Offense Type'] = df17['Offense Type'].str.strip()
.
.

df17['Offense Type'].unique()

array(['Burglary', 'Theft', 'Robbery', 'Auto Theft', 'Aggravated Assault',
       'Rape', 'Murder', 'AutoTheft', nan], dtype=object)
```

## Problem

Similar values with small variation.


```python
df17['Offense Type'].value_counts(dropna=False)

Theft                 67422
Burglary              17084
Aggravated Assault    12314
Robbery                9778
AutoTheft              7627  # <--- Same values
Auto Theft             3874  # <--- Same values
Rape                   1368
Murder                  258
NaN                       2
Name: Offense Type, dtype: int64
```

## Solution:

Use the [pandas.Series.str.replace](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.str.replace.html) to replace the value


```pyton
df17 = df17.replace('Auto Theft','AutoTheft')
.
.
Theft                 67422
Burglary              17084
Aggravated Assault    12314
AutoTheft             11501
Robbery                9778
Rape                   1368
Murder                  258
NaN                       2
Name: Offense Type, dtype: int64
```


## Problem:
Converting date column to datetime
```python
df17.info()

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 119727 entries, 0 to 119726
Data columns (total 8 columns):
Date            119727 non-null object
Beat            119727 non-null object
BlockRange      119727 non-null object
StreetName      119718 non-null object
Offense Type    119725 non-null object
Premise         119240 non-null object
Offenses        119727 non-null float64
Hour            119727 non-null int64
dtypes: float64(1), int64(1), object(6)
memory usage: 7.3+ MB
```

## Solution:
- [pandas.to_datetime](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.to_datetime.html)
- [pandas.DataFrame.set_index](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.set_index.html)
- [pandas.DataFrame.sort_index](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_index.html)
```python
df17['Date'] = pd.to_datetime(df17['Date'])

df17 = df17.set_index('Date').sort_index(ascending=True)
```

```python
df17.info()


<class 'pandas.core.frame.DataFrame'>
DatetimeIndex: 119727 entries, 1917-01-20 to 2017-12-31
Data columns (total 7 columns):
Beat            119727 non-null object
BlockRange      119727 non-null object
StreetName      119718 non-null object
Offense Type    119725 non-null object
Premise         119240 non-null object
Offenses        119727 non-null float64
Hour            119727 non-null int64
dtypes: float64(1), int64(1), object(5)
memory usage: 7.3+ MB
```


## Problem
Columns with similar yet diffrent names from diffrent datasets.

- `Block Range` &  `BlockRange`
- `Street Name`  & `StreetName`
- `# offenses` & `Offenses`

```python
df1.columns


Index(['# offenses', 'Beat', 'Block Range', 'BlockRange', 'Date', 'Hour',
       'Offense Type', 'Offenses', 'Premise', 'Street Name', 'StreetName',
       'Suffix', 'Type'],
      dtype='object')
```

## Solution:

- [pd.concat](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.concat.html)
- [pandas.DataFrame.dropna](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.dropna.html)
- [pandas.DataFrame.reindex_like](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.reindex_like.html)


```python
df1['BlockRange'] = pd.concat([df1['Block Range'].dropna(), 
                               df1['BlockRange'].dropna()]).reindex_like(df1)

df1['StreetName'] = pd.concat([df1['Street Name'].dropna(),
                               df1['StreetName'].dropna()]).reindex_like(df1)

df1['Offenses'] = pd.concat([df1['# offenses'].dropna(),
                             df1['Offenses'].dropna()]).reindex_like(df1)
```

## Problem

Data sets has odd dates

```python
df16.info()


# index should be from 2016-01-01 to 2016-12-31
<class 'pandas.core.frame.DataFrame'>
DatetimeIndex: 122693 entries, 1916-05-23 to 2016-12-31 # <-- 1916-05-23 ???
Data columns (total 7 columns):
Beat            122693 non-null object
BlockRange      122693 non-null object
StreetName      122655 non-null object
Offense Type    122689 non-null object
Premise         121293 non-null object
# offenses      122693 non-null int64
Hour            122693 non-null int64
dtypes: int64(2), object(5)
memory usage: 7.5+ MB
```

## Solution

create a selection with the dates you want

```python
df2016 = df16.loc['2016-01-01':'2016-12-31'] 
```
```python
df2016.info()

<class 'pandas.core.frame.DataFrame'>
DatetimeIndex: 121421 entries, 2016-01-01 to 2016-12-31
Data columns (total 7 columns):
Beat            121421 non-null object
BlockRange      121421 non-null object
StreetName      121383 non-null object
Offense Type    121419 non-null object
Premise         120072 non-null object
# offenses      121421 non-null int64
Hour            121421 non-null int64
dtypes: int64(2), object(5)
memory usage: 7.4+ MB
```


## Problem
Need to load multiple files into one dataframe

```bash
$ ls crime_data_raw/2012

apr12.xls*  dec12.xls*  jan12.xls*  jun12.xls*  may12.xls*  oct12.xls*
aug12.xls*  feb12.xls*  jul12.xls*  mar12.xls*  nov12.xls*  sep12.xls*
```
## Solution:

expl.

```python
path = 'crime_data_raw/2012'
all_files = glob.glob(os.path.join(path, "*.xls")) 

df_from_each_file = (pd.read_excel(f) for f in all_files)
df   = pd.concat(df_from_each_file, ignore_index=True)
```

## Problem

Column has many values with extra characters.

- some teams have ranking values next to the names


```python
len(rice.Opponent.unique())

51
```

```python
rice.Opponent.unique()
.
.
array(['SMU', 'Memphis', 'Vanderbilt', '(7) Texas', 'North Texas',
       'Tulsa', 'Southern Mississippi', 'Tulane', 'UTEP', 'Army',
       'Marshall', 'Houston', 'Western Michigan', 'UAB', 'Texas Tech',
       '(16) Oklahoma State', 'Navy', 'East Carolina', 'UCF',
       '(25) Houston', '(5) Texas', 'Northwestern', 'Baylor', 'Texas',
       'Purdue', '(17) Baylor', '(18) Houston', 'UCLA', 'Kansas',
       'Louisiana Tech', 'UTSA', 'Air Force', '(7) Texas A&M',
       'Florida Atlantic', 'New Mexico State', 'Mississippi State',
       '(17) Notre Dame', 'Old Dominion', 'Hawaii',
       'Florida International', '(21) Marshall', 'Fresno State', 'Wagner',
       '(5) Baylor', 'Western Kentucky', 'Charlotte', '(21) Baylor',
       'Prairie View A&M', 'Stanford', '(14) Stanford', 'Pitt'],
      dtype=object)
```

## Solution:
- Use the [pandas.Series.str.replace](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.str.replace.html) to replace the value

- Regular expressions!
- we want to match `(##)` a paranthesis with numbers inside.
- `r"\(.*\)"` 
    - match a "(" `\(` 
    - folowed by `.*` a string of various lenght 
    - and  ")" `\)`

- Call the [pandas.Series.str.strip](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.str.strip.html) to remove any white spaces

```python
rice['Opponent'] = rice['Opponent'].str.replace(r"\(.*\)"," ").str.strip()
```

```python
len(rice.Opponent.unique())
42
```

```python
rice.Opponent.unique()

array(['SMU', 'Memphis', 'Vanderbilt', 'Texas', 'North Texas', 'Tulsa',
       'Southern Mississippi', 'Tulane', 'UTEP', 'Army', 'Marshall',
       'Houston', 'Western Michigan', 'UAB', 'Texas Tech',
       'Oklahoma State', 'Navy', 'East Carolina', 'UCF', 'Northwestern',
       'Baylor', 'Purdue', 'UCLA', 'Kansas', 'Louisiana Tech', 'UTSA',
       'Air Force', 'Texas A&M', 'Florida Atlantic', 'New Mexico State',
       'Mississippi State', 'Notre Dame', 'Old Dominion', 'Hawaii',
       'Florida International', 'Fresno State', 'Wagner',
       'Western Kentucky', 'Charlotte', 'Prairie View A&M', 'Stanford',
       'Pitt'], dtype=object)
```

## Problem
You need to rename columns in your dataframe

```python
astros.head()


full_date   Tm  R Unnamed: 5  Opp  RA W/L Attendance
0 2008-03-31  HOU  0          @  SDP   4   L     44,965
1 2008-04-01  HOU  1          @  SDP   2   L     20,825
2 2008-04-02  HOU  9          @  SDP   6   W     18,714
3 2008-04-03  HOU  2          @  SDP   3   L     24,432
4 2008-04-04  HOU  4          @  CHC   3   W     37,812


```

[pandas.DataFrame.rename](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html) to change the columns

```python
astros.rename(columns={'full_date': 'date',
                       'Tm': 'team',
                       'R':'team_score',
                       'Unnamed: 5':'home_away',
                      'Opp': 'opposing',
                      'RA':'opp_score',
                      'W/L':'win_lost',
                      'Attendance':'attendance'}, inplace=True)
```


```python
astros.head()


date team  team\_score home\_away opposing  opp\_score win\_lost  \
0 2008-03-31  HOU           0         @      SDP          4        L   
1 2008-04-01  HOU           1         @      SDP          2        L   
2 2008-04-02  HOU           9         @      SDP          6        W   
3 2008-04-03  HOU           2         @      SDP          3        L   
4 2008-04-04  HOU           4         @      CHC          3        W   

  attendance  
0     44,965  
1     20,825  
2     18,714  
3     24,432  
4     37,812
```


## Problem
You have a column that should display `home` or `away`, but instead it displays `@` or `Nan`.

```python
astros[['home_away', 'opposing']].head()


home_away opposing
date                         
2008-03-31         @      SDP
2008-04-01         @      SDP
2008-04-02         @      SDP
2008-04-03         @      SDP
2008-04-04         @      CHC
```

## Solution

- inspect values
- [np.where](https://docs.scipy.org/doc/numpy/reference/generated/numpy.where.html) to change based on condition.

```python
astros['home_away'].unique()

 array(['@', nan], dtype=object)
```


```python
astros['home_away'].value_counts(dropna=False)

@      810
NaN    809
Name: home_away, dtype: int64
```
Change values base on condition

```python

astros['home_away'] = np.where(astros['home_away'] =='@', 'AWAY', 'HOME')


astros[['home_away', 'opposing']].head()



home_away opposing
date                         
2008-03-31      AWAY      SDP
2008-04-01      AWAY      SDP
2008-04-02      AWAY      SDP
2008-04-03      AWAY      SDP
2008-04-04      AWAY      CHC
```












## Problem

You have two columns and you need to join them.

```python
df[['BlockRange','StreetName']].head(10)

BlockRange          StreetName
0         6900-6999             TRIGATE
1         4200-4299         SAN JACINTO
2           800-899      WEST OAKS MALL
3         5700-5799            LOCKWOOD
4         1700-1799           CHENEVERT
5         6400-6499         TALL WILLOW
6           500-599       BAYBROOK MALL
7         7900-7999              AMELIA
8         5400-5499           ALLENDALE
9         1200-1299            COMMERCE
```

### Solution
- [pandas.DataFrame.apply](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.apply.html)
- lamda function that joins values with a space in between.

```python
df['address'] = df[['BlockRange', 'StreetName']].apply(lambda x: ' '.join(x), axis=1)
```

```python
df[['BlockRange','StreetName','address']].head(10)


  BlockRange      StreetName                 address
0  6900-6999         TRIGATE       6900-6999 TRIGATE
1  4200-4299     SAN JACINTO   4200-4299 SAN JACINTO
2    800-899  WEST OAKS MALL  800-899 WEST OAKS MALL
3  5700-5799        LOCKWOOD      5700-5799 LOCKWOOD
4  1700-1799       CHENEVERT     1700-1799 CHENEVERT
5  6400-6499     TALL WILLOW   6400-6499 TALL WILLOW
6    500-599   BAYBROOK MALL   500-599 BAYBROOK MALL
7  7900-7999          AMELIA        7900-7999 AMELIA
8  5400-5499       ALLENDALE     5400-5499 ALLENDALE
9  1200-1299        COMMERCE      1200-1299 COMMERCE
```


## Problem
Neet to create a column with  latitude and longtitude values from a given address.

```python
df[['address']]

Date
2013-01-01         6900-6999 TRIGATE
2013-01-01     4200-4299 SAN JACINTO
2013-01-01    800-899 WEST OAKS MALL
2013-01-01        5700-5799 LOCKWOOD
2013-01-01       1700-1799 CHENEVERT
2013-01-01     6400-6499 TALL WILLOW
2013-01-01     500-599 BAYBROOK MALL
2013-01-01          7900-7999 AMELIA
2013-01-01       5400-5499 ALLENDALE
2013-01-01        1200-1299 COMMERCE
Name: address, dtype: object


```

## Solution
- get api key from [google maps](https://developers.google.com/maps/)
- write a function that takes in a partial address and returns a lat long tuple
- apply to series(or dataframe column)

```python
def get_geocode(loc,key):
    '''input: partial address and api key
        return: tuple with lat and long'''
    address = '{}, Houston, TX'.format(loc)  #can be change
    pa = {'address': address, 'key':key}
    URL = 'https://maps.googleapis.com/maps/api/geocode/json'
    response = requests.get(URL,params=pa)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        return "Error: " + str(e) # not 200
    js_obj = response.json()
    if js_obj['status'] == 'OK':
        gps = tuple(js_obj['results'][0]['geometry']['location'].values())
        return gps
    elif js_obj['status'] =='OVER_QUERY_LIMIT':  # too many calls
        return np.nan
    else:
        print(js_obj['status'])
        return js_obj['status']
```

Apply function

```python
df['lat_lng'] = df['address'].apply(get_geocode,args=(API_KEY,))
```

```python
df[['address','lat_lng']]

address                    lat_lng
Date                                                         
2013-01-01       6900-6999 TRIGATE  (29.5932746, -95.4886236)
2013-01-01   4200-4299 SAN JACINTO  (29.7338398, -95.3802958)
2013-01-01  800-899 WEST OAKS MALL  (30.0062716, -95.4149863)
2013-01-01      5700-5799 LOCKWOOD   (29.811049, -95.3170506)
2013-01-01     1700-1799 CHENEVERT   (29.7475636, -95.362194)
2013-01-01   6400-6499 TALL WILLOW  (29.8677163, -95.4880834)
2013-01-01   500-599 BAYBROOK MALL   (29.5421873, -95.148344)
2013-01-01        7900-7999 AMELIA  (29.8072157, -95.4855513)
2013-01-01     5400-5499 ALLENDALE  (29.6832373, -95.2408037)
2013-01-01      1200-1299 COMMERCE  (29.7626002, -95.3577339)
```

## Problem
Need to display lat lon coordinates into a map inside a jupyter notebook

## Solution

[gmaps](https://github.com/pbugnion/gmaps): a python library that does just that

Create a variable with our data.
```python
locations = df['lat_lng']


locations


Date
2013-01-01    (29.5932746, -95.4886236)
2013-01-01    (29.7338398, -95.3802958)
2013-01-01    (30.0062716, -95.4149863)
2013-01-01     (29.811049, -95.3170506)
2013-01-01     (29.7475636, -95.362194)
2013-01-01    (29.8677163, -95.4880834)
2013-01-01     (29.5421873, -95.148344)
2013-01-01    (29.8072157, -95.4855513)
2013-01-01    (29.6832373, -95.2408037)
2013-01-01    (29.7626002, -95.3577339)
Name: lat_lng, dtype: object

```

Display it on a map

```python
fig = gmaps.figure()
markers = gmaps.marker_layer(locations)
fig.add_layer(markers)
fig
```
![map](./Houston_Crime_Data/img/map2.png)
 what if you wanted a heat map version
 
 ```python
fig = gmaps.figure()
fig.add_layer(gmaps.heatmap_layer(locations))
fig
```

![map](./Houston_Crime_Data/img/map_heat.png)