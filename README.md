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
        - [MetaBase](#metabase)
        - [PostgreSQL](#postgresql)
- [Scripts Description](#scripts)
    - [Extraction from API](#api-extraction)
    - [Go to the Import View](#go-to-the-import-view)
    - [Upload the page tree file](#upload-the-page-tree-file)
    - [Go to the import view](#go-to-the-import-view)
    - [Import the page tree](#import-the-page-tree)
    - [SEO-friendly URLs](#seo-friendly-urls)
- [License](#license)
- [Links](#links)

------
## Installation

### Neural Prophet
**Note:** neural-prophet is required!

The latest version can be installed via PIP or conda prompt, version might be dependent on your python environment. Latest release is recommended. This process is automated on most systems and can be executed with following terminal command:

```bash
pip install neural-prophet
```


### Additional Installations
**Note:** These installations are not necessary to run the vanilla version of the project but are recommended to get installation of an interactive **MetaBase Dashboard** up and running.

### MetaBase
The latest release of metabase can be downloaded using the following automated command line argument:
````bash
wget http://downloads.metabase.com/v0.46.0/metabase.jar
````
**Note:** Eclipse JAVA runtime should be installed on the system

### PostgreSQL
This is a database packaged installation. The database is used as a backend for MetaBase, So this is the pre-requisite in order to run a successful MetaBase instance.

**The platform specific binaries and packages can be found on [PostgreSQL](https://www.postgresql.org/download/) website.**

-----
## Scripts
### API-Extraction
