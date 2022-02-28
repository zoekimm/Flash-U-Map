# Flash-U-Map

This web application serves as a "safety guidance map" where one can enter the estimated time and location to see whether the place is likely safe or not. 

## Built With

* googlemaps==4.6.0
* matplotlib==3.5.1
* matplotlib-inline==0.1.3
* scikit-learn==1.0.2
* seaborn==0.11.2
* sklearn==0.0
* streamlit-folium==0.6.2

## Inspiration
The idea for this application came across when reading the [BBC article](https://www.bbc.com/news/57581270) 'US crime: Is America seeing a surge in violence?'; the article stated that the number of violent crime cases went up by about 3% in 2020 over the past year. United States is known for its high crime rate compared to other countries located in Europe and Asia. According to the Bureau of Justice Statistics, the crime rate for robbery in the United States is 4 times higher than that of Europe. To ensure the safety of the community, this application will help the user to be conscious of where they are heading to. 

## What it does
* Users can enter the location and the estimated time of arrival.
* The machine-learning model will evaluate whether the location is likely to be "safe" or "not safe" based on the user's input.
* The model was trained with 610329 data points and achieved an accuracy score of 0.8364. 
* Users can also get a glance of the city through the heat map of nearby locations and from the daily update of cases within the city.
* To give users more information, plots ranging from count plot to heat map are displayed on the website.

## How we built it
1. Dataset downloaded from [Kaggle](https://www.kaggle.com/vinchinzu/dc-metro-crime-data)
2. Data Preprocessing and Cleaning
3. Model Building (RandomForestClassifier, DecisionTreeClassifier)
4. Front-End Development with StreamLit
5. Connecting Google-Map-API to the website
6. Model Deployment

## Challenges
Since this was the first time deploying a machine-learning model and launching into an website, it took some time to get everything aligned and use the model in the Streamlit framework. 

## Accomplishments 
- Going beyond from building a machine learning model
- Deploying a machine-learning model into a web application
- Working on everything from scratch -- data preprocessing, model building to web application

## What we learned


## What's next for Flash-U-Map
