# Site-Energy-Intensity-Prediction
Site Energy prediction Machine Learning streamlit deployment
Description:

According to a report issued by the International Energy Agency (IEA), the lifecycle of buildings from construction to demolition were responsible for 37% of global energy-related and process-related CO2 emissions in 2020.

Yet it is possible to drastically reduce the energy consumption of buildings by a combination of easy-to-implement fixes and state-of-the-art strategies.

The dataset consists of building characteristics, weather data for the location of the building, as well as the energy usage for the building and the given year, measured as Site Energy Usage Intensity (Site EUI).
This data set is collected from The WiDS Datathon 2022 which focuses on a prediction task involving roughly 100k observations of building energy usage records collected over 7 years and a number of states within the United States.
🧭 Problem Statement:

In this project, regression-based performance prediction model was developed to estimate building energy consumption based on simplified façade attribute information and weather conditions. Building façade features, including floor_area, elevation, energy star ratings, year_built, year_factor, state_factor, building_class, facility_type etc., were collected over 7 years and a number of states within the United States. Based on this training dataset, a prediction model was established to estimate annual energy use. The developed estimation model adopted architectural physical attributes and their dynamic ambient environmental conditions as input variables. This prediction approach will provide a more specific baseline and goal especially in the pre-design phase, it also could asses EUI by a minimum amount of data.
📊 Exploratory Data Analysis:

    Exploratory Data Analysis is the first step of understanding your data and acquiring domain knowledge.
    On using Shapiro-Wilk test it was found that majority of features were not following normal distribution.
    There was no outliers found using Z-Score estimation and IQR.

⌛ Data Preprocessing:

    Used KNN Imputer to impute missing values.
    Used LabelEncoder & TargetEncoder of encoding categorical features in dataset.

🔎 Features Selection:

    On using Pearson's Correlation test, it was found that many features were highly correlated. So I removed the features with collinearity.

⚙ Model Training:

    On training my model using several regression algorithms, the model trained with XGBoost Regressor gave best results.
   
Web Application 💻 🌎 :
