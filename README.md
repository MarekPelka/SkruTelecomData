# Systems Of Mobile Communication - student project

Visualisation of converted data from telecommunication database.
Viewer can take a look on in/out sms numbers, calls and internet traffic in Milan city (optional Trento).
Projects is made in Java Script (visualisation) and Spring MVC (back-end).

## Reviewers: 

* **Grzegorz Przytuła** - *Initial work, python scripts, Java (Spring MVC, Hibernate, Maven)* - [gpr95](https://github.com/gpr95)
* **Marek Pelka** - *Java Script* - [marekpelka](https://github.com/marekpelka)

## Installation steps:

### 1 Download datasets:
* [Milano Grid](https://dandelion.eu/datamine/open-big-data/) - geographical segmentation of the city in order 
to aggregate the measurements of the other datasets. The area of each square is 55225-m2 and it has 10000 
squares in the form of a (x, y) point and the latitude and longitude belonging to this x, y point.


## DUMPING FULL DATA

### 2 Replace end-of-file symbols with python script:
```
python/01_replace_carriage_return_full
```
### 3 Create database `skru` in mysql localhost and execute sql:
```
sql/milano.sql
sql/trento.sql
```
### 4 Dump data with script:
```
python/02_dump_full_data
```
## DUMPING CONVERTED DATA

### 5 Split downloaded files with python scripts:
```
python/03_split_milano_november_2013_into_hourly_files
python/03_split_milano_december_2013_into_hourly_files
```
### 6 Replace end-of-file symbols with python script:
```
python/05_replace_carriage_return_converted
```
### 7 Dump data with script:

```
python/06_dump_converted
```

