<img src='./logo.gif'> <img src='./CaBi-logo_red.png'>
## Bike Sharing Enterprise 

### Inception
This is a project of analysis of available data from the Bike Sharing company. 
Bike sharing is based in the public bicycle scheme. It is a service to share use to individuals on a short term basis for a price or free. The scheme of sharing bikes allows people to borrow a bike from a "dock" and return it at another dock belonging to the same system.

Companies page: https://www.capitalbikeshare.com/

UCI dataset Repository: https://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset


### Problem description

Docks are the special bike racks that lock the bike, and only release it by computer control. The logistics process focuses on the activities of providing "docks" in appropriate zones, allowing convenient access to equipment for any potential user. 
In the analyse we were analyzed external areas, get to know what affects the size of the demand.

### Data set

The data was collected in order to analyze the external phenomena of the company from the UCI data collection repository.

Author of data set: Hadi Fanaee-T - Laboratory of Artificial Intelligence and Decision Support (LIAAD), University of Porto

Author of data analysis: mikey.prus@gmail.com


### Data description 
This dataset contains the hourly and daily count of rental bikes between years 2011 and 2012 in Capital bikeshare system with the corresponding weather and seasonal information.


<img src='./data.png'>

### Data Records

- instant: record index
- dteday : date
- season : season (1:winter, 2:spring, 3:summer, 4:fall)
- yr : year (0: 2011, 1:2012)
- mnth : month ( 1 to 12)
- hr : hour (0 to 23)
- holiday : weather day is holiday or not (extracted from [Web Link])
- weekday : day of the week
- workingday : if day is neither weekend nor holiday is 1, otherwise is 0.

+ weathersit :
- 1: Clear, Few clouds, Partly cloudy, Partly cloudy
- 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
- 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
- 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
- temp : Normalized temperature in Celsius. The values are derived via (t-t_min)/(t_max-t_min), t_min=-8, t_max=+39 (only in hourly scale)
- atemp: Normalized feeling temperature in Celsius. The values are derived via (t-t_min)/(t_max-t_min), t_min=-16, t_max=+50 (only in hourly scale)
- hum: Normalized humidity. The values are divided to 100 (max)
- windspeed: Normalized wind speed. The values are divided to 67 (max)
- casual: count of casual users
- registered: count of registered users
- cnt: count of total rental bikes including both casual and registered

### Technologies
* pandas
* matplotlib.pyplot

### Goal

* The effect of external factors on the size of demand.

* Provide convenient access to equipment for any potential user. 



