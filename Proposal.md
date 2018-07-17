
# Proposal for Capston Project

**Title**: Predicting the likelihood of a crime around a sports stadium in the city of Houston Texas.


## Problem
Imagine,  you just got tickets for the playoffs and you start making plans on what bar around the stadium  y'all are goin to "pre-game" 
when  your friend tells you that crime around the stadium is high when there is a game and that we should be carefull.  Without calling your friend out on guessing, you reply that there are many factors such as  sports team schedule,date, time, orgin of a crime and distance from the stadium etc. which migh affect the crime rate. 
Given that, I propose to use data from varius sources containing these factors and build a macine learning model for predicting the likehood of crime around sports arena from  several Houston sports teams.

## Client  
    > needs fixin

Cupidatat ad id mollit anim cillum. In adipisicing est pariatur ad enim ut eiusmod sint magna ut dolor ullamco adipisicing fugiat. Nulla nostrud pariatur in incididunt in in. Mollit elit tempor laborum deserunt.

Magna eiusmod aliqua velit officia voluptate deserunt aliquip elit esse tempor ipsum elit qui. Ex eu incididunt aliqua qui veniam aliquip. Non culpa minim dolore sit duis aliqua consequat quis officia enim. Laborum qui velit sint ex ad exercitation incididunt laborum magna exercitation. In consectetur anim ex proident dolor ex ea anim in aliqua qui nulla. Adipisicing velit ut nostrud aute non.

## Data
Houston has a rich sporting culture with five professional major league teams and two Division I college athletic programs. Datasets for sports teams will be a date aschedule from 2010 to 2017 of local games played, score and opposing team.

The crime data is provided by the [Uniform Crime Reporting program](https://en.wikipedia.org/wiki/Uniform_Crime_Reports) or UCR. It compiles official data collected by law enforcement agencies across the United States. UCR criminal offenses are divided into two major groups, Part I and Part II. 

Part I offenses are considered to be serious and are broken into two categories: violent and property crimes, those include murder, rape, robbery, aggravated assault, burglary, theft, and auto theft. 

Part II offenses are all crimes classifications other than those defined as Part I, some of those include: other assaults, forgery, fraud, vandalism, prostitution, disorderly conduct. 

[Houston police department](http://www.houstontx.gov/police/cs/index-2.htm) provides crime statistics for several years dating back to 2005, datasets from Part I offenses from 2010 to 2017 will be used to find the type of crime around a sporting event given its stadium location. 
 

## Approach

Since the main purpose is to predict the likelyhood of crime given spots arena, supervised regression will be used to build thepredictve model. Several regression model will be used a "trow what sticks" approach will be used.


## Limitations

The prediction of the model will depend on how good the crime dataset is,


In other words. if we want to predict the likelihood of crime around stadium, some crimes are not reported untill days later or not even at all.  Time of the crime could also afect the result,  a police report might write down the time the crime is reported and not when it actually happen.



## Deliverables

1. Jupyter notebooks for 
    - data acquisition
    - data cleaning
    - data exploration analysis
    - machine learing model development.



2. Report on the capston eproject
3. Presentation of the capstone project.