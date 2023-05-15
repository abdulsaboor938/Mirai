![Logo](https://github.com/abdulsaboor938/Mirai/blob/74d06816a52fbb56f218cb84c84be3efe1a130fe/images/logo-banner.png)

# Mirai
This project aims to predict the occurrence of photochemical smog, commonly known as smog, in specific areas or regions worldwide. The goal is to develop an application that combines real-time air pollution and weather data to provide accurate and timely predictions of smog intensity and timing. The project is in its early stages, with a focus on achieving accurate predictions based on the collected dataset.

The dataset is being collected using APIs from sources such as OpenWeatherMap and Open-Meteo. These APIs provide information on various air pollutants (aqi, co, no, no2, o3, so2, pm2_5, pm10, and nh3) as well as temperature and dew point. The data is pre-processed and merged from both sources, ensuring synchronization of date and location coordinates.

To achieve accurate predictions, several models were evaluated, including SARIMAX, Neural Prophet, Multivariable Adversarial Learning, and various LSTM variants based on permissible time. While the code for the dataset is being built from scratch, the performance of the prediction algorithm will be based on existing libraries and code snippets available on the internet, with proper references provided. The most accurate predictions were obtained from Neural Prophet.

Once the accurate prediction of smog patterns is achieved, the project aims to develop an application that allows users to visualize past data trends and future forecasts. The combination of air pollution and weather data in real-time analytics can provide valuable insights for understanding and addressing the issue of smog.

-----
## Table Of Content

- [Initial Setup](#installation)
    - [Neural Prophet](#neural-prophet)
    - [Addtional Dependencies](#additional-installations)
        - [Metabase](#metabase)
        - [PostgreSQL](#postgresql)
- [Scripts Description](#scripts)
    - [Extraction from API](#api-extraction)
    - [Machine Learning Model](#model)
        - [Training](#model-training)
        - [Evaluation](#model-evaluation)
        - [Predictions](#predictions)
- [Visualizations](#visualizations)
    - [Database Setup](#database-setup)
    - [Metabase](#metabase)
- [Authors](#authors)
- [Acknowledgements](#acknowledgements)

------
## Installation

### Neural Prophet
**Note:** neural-prophet is required!

The latest version can be installed via PIP or conda prompt, version might be dependent on your python environment. Latest release is recommended. This process is automated on most systems and can be executed with following terminal command:

```bash
pip install neural-prophet
```


### Additional Installations
**Note:** These installations are not necessary to run the vanilla version of the project but are recommended to get installation of an interactive **Metabase Dashboard** up and running.

### Metaase
The latest release of metabase can be downloaded using the following automated command line argument:
````bash
wget http://downloads.metabase.com/v0.46.0/metabase.jar
````
**Note:** Eclipse JAVA runtime should be installed on the system

### PostgreSQL
This is a database packaged installation. The database is used as a backend for Metabase, So this is the pre-requisite in order to run a successful Metabase instance.

**The platform specific binaries and packages can be found on [PostgreSQL](https://www.postgresql.org/download/) website.**

-----
## Scripts
### API-Extraction
**Note:** To get this project running, you will need [OpenweatherMap's](https://home.openweathermap.org/api_keys) API key. This can be done by creating a trial account. THough a premium plan with higher API call limits is recommended in order to run this as a live environemnt.

Once API key is obtained, it can be updated in **api_key** environment variable, found in the beginning of ***1.API_extract.ipynb***

`api_key`

This script gathers multiple API responses based on the coordinates and cities defined in following environment variables:

`coordinates` This is an array of all longitudes and latitudes of the city, each corresponding to a predefined **zone**.

`cities` This is an array containing the **names of the cities** coorresponding all zonal coordinates in the coordinates environment variable.

**1. OpenWeatherMap**
```JSON
{"coord":
    {"lon":41.0193,"lat":43.0034},
    "list":
    [
        {"main":{"aqi":1},
            "components":{"co":211.95,"no":0,"no2":0.48,"o3":53.64,"so2":0.03,"pm2_5":1.09,"pm10":1.25,"nh3":0.85},
        "dt":1609459200},
        {"main":{"aqi":1},
            "components":{"co":211.95,"no":0,"no2":0.52,"o3":55.79,"so2":0.03,"pm2_5":1.11,"pm10":1.26,"nh3":0.91},
        "dt":1609462800}
    ]
}
```

**2. Meteo**
```JSON
{
    "latitude":43.0,
    "longitude":41.0,
    "generationtime_ms":18.211007118225098,
    "utc_offset_seconds":0,
    "timezone":"GMT",
    "timezone_abbreviation":"GMT",
    "elevation":14.0,
    "hourly_units":{"time":"iso8601","temperature_2m":"°C","dewpoint_2m":"°C"},
    "hourly":{
        "time":["2021-01-01T00:00","2021-01-01T01:00"],
        "temperature_2m":[5.5,4.3],
        "dewpoint_2m":[2.0,1.5]
    }
}
````
***OpenWeatherMap was only used to collect the pollutants data and hence Meteo is used to collect `temperature` and `dewpoint` information for the corresponding entries.***

### Compilation

The data is collected from `January 1, 2021` to current data. When following this format, The API call returns `8760` entries for each year.
This data is collected into 10 csv files, each with `500,000+` entries. *This was done to enable parallel extraction and save valuable time in the live enviroment.*
These files are named **1** to **10** resepctively and are stored in the `Batch Data` folder.

![raw_data](https://github.com/abdulsaboor938/Mirai/blob/c8787d5070ab625c21686404efcdbbca7836a75a/images/Screenshot%202023-05-16%20at%2012.23.53%20AM.png)

The `raw_data.csv` is a compiled file of all the `5,000,000+` entries. This is the file used for model training and further processing. The file is described as following:

`date` The human readable timestamp.

`zone` The city's zone **(1-248)**.

`longitude` `latitude`

`temperature` `pm10` `pm2_5` The quality paramaeters.

`smog` This is based on the intuition that when maximum value of `pm10 & pm25` is greater than `300` and temperature is less than `25 Celcius`.

-----

## Model

### Model Training

This module describes the implementation of the ***2.Model.ipynb*** file.

Following Steps are implemented in this file:

**Extracting Single City**
To gain higher accuracy in results, models are trained for each city separately and then predictions are compiled into one singular format. The first step is to get the data of a single city. This is simply an abstraction of the `raw_data.csv` on the basis of city's zonal separation.

![SIngle City](https://github.com/abdulsaboor938/Mirai/blob/c8787d5070ab625c21686404efcdbbca7836a75a/images/Screenshot%202023-05-16%20at%2012.23.53%20AM.png)

**Model training for `Temperature` `pm10` `pm25`**

Now that we have obtained a raw representation of data, its time to apply the model. After the pre-processing steps involving `train-test split` and creation of the `ds` and `y` column. We have a following representation.

![training_data](https://github.com/abdulsaboor938/Mirai/blob/1faea581515a83ae86777b29299f7ff6f475ac66/images/Screenshot%202023-05-16%20at%2012.51.45%20AM.png)

Viola! We have made it to model training, which is defined as following:
```Python
from neuralprophet import NeuralProphet, set_log_level
set_log_level("ERROR")

m = NeuralProphet(
    changepoints_range=0.95,
    n_changepoints=24,
    trend_reg=1,
    weekly_seasonality=False,
    daily_seasonality=1,
    seasonality_mode="multiplicative",
)
```
A multiplicative model is applied to better capture the changes in trend over a 24-hour period, 95th percentile of data.

Tough the model works in most efficient manner, a parallel kernel split is recommneded to speed up the training process.

![parallel Training](https://github.com/abdulsaboor938/Mirai/blob/389787549f57dd5bc46ef3384cfb84090c38364d/images/Screenshot%202023-05-13%20at%2011.40.14%20AM.png)

A need to parallel processing was deemed necessary in order to compensate for expense of training required. Each parameter requires compilation of a `20gb` model. This equates to `60gb (20*3)` training for each city, equating to a total of `15TB` of training.

***The demo training was carried out on 2 Mac machines, split across 3 kernels on each machine. Overall training time on Apple's M1 Neural engine was around 2 hours (per machine).***

### Model Evaluation
**Training Error**
![Training Error](https://github.com/abdulsaboor938/Mirai/blob/389787549f57dd5bc46ef3384cfb84090c38364d/images/Screenshot%202023-05-16%20at%201.05.31%20AM.png)

### Predictions

Once model is validated for training error. The predictions are combine into a file along with original data values. This file is created by concatenating `raw_data` and `prediction` folder's files. The newly generated file is stored as `final_data.csv`

**Note: The final form of data is not included in this repository due to Github's Size limitations.**

-----

## Visualizations

### Database

We have made it through the difficult part of this implementation. Its time to give yourself a cheer!

Now run the downloaded **PostgreSQL** database server and connct it with the IDE of your choice. Here, Jetbrain's DataGrip IDE was used in conjunction with PosgreSQL's Mac Distribution to simply load the `final_data.csv` file into `postrgre` schema.

![postgreSQL-server](https://github.com/abdulsaboor938/Mirai/blob/c15ec877029187ac23fbf951284f705f6bcdcc35/images/Screenshot%202023-05-16%20at%201.24.16%20AM.png)

![DataGrip](https://github.com/abdulsaboor938/Mirai/blob/125cb8f01aef7507379e75cdc39fa0f15c18dfd7/images/Screenshot%202023-05-14%20at%201.46.24%20AM.png)

Once this is done, the only thing left is to run `Metabase` and drill through the visualizations to acquire any additional details about the data.

### Metabase

Head over the directory where you downloaded the Metabase Jar file in [this](#additional-dependencies) step. Open a terminal window in that directory and type in the following command:
```bash
!java -jar metabase.jar
```

Or you can alternatively run this command in any folder of your choice, If Metabase not downloaded already. **Eclipse's JAVA runtime should be installed**
```bash
# check if metabase.jar is present, if not download it
if [ ! -f metabase.jar ]; then
    wget https://downloads.metabase.com/v0.46.0/metabase.jar
fi

# run metabase
java -jar metabase.jar
```

**Phew! That was quite hectic.**

Wait a few settings and once Metabase is running, headover to `localhost:3000` to access `Metabase`

Head over to `admin settings -> databases` and configure teh database as following:
![database connection](https://github.com/abdulsaboor938/Mirai/blob/125cb8f01aef7507379e75cdc39fa0f15c18dfd7/images/Screenshot%202023-05-16%20at%201.25.07%20AM.png)

`GOOD LAD`

You've made it through, enjoy beautiful visualizations and dashboards like this, representing both `historical data` and `7-day forecast`. **Remember to play-around and try to find answers to your curious questions.**

![](https://github.com/abdulsaboor938/Mirai/blob/e9f9306bada38fc240a43ce33c8d2fe352ff94ae/images/Screenshot%202023-05-16%20at%201.41.33%20AM.png)
![](https://github.com/abdulsaboor938/Mirai/blob/e9f9306bada38fc240a43ce33c8d2fe352ff94ae/images/Screenshot%202023-05-16%20at%201.41.45%20AM.png)
![](https://github.com/abdulsaboor938/Mirai/blob/e9f9306bada38fc240a43ce33c8d2fe352ff94ae/images/Screenshot%202023-05-16%20at%201.42.33%20AM.png)
![](https://github.com/abdulsaboor938/Mirai/blob/e9f9306bada38fc240a43ce33c8d2fe352ff94ae/images/Screenshot%202023-05-16%20at%201.42.51%20AM.png)

-----

## Authors
[@abdulsaboor938](https://github.com/abdulsaboor938)
[@minalurooj](mailto:l201388@lhr.nu.edu.pk)

-----

## Acknowledgements

- [OpenWeatherMap](https://openweathermap.org/)
- [Open-Meteo](https://open-meteo.com/)
- [NeuralProphet](https://neuralprophet.com/)

-----

To contribute to the [Mirai](https://github.com/abdulsaboor938/Mirai) project, check out <https://github.com/abdulsaboor938/Mirai>
