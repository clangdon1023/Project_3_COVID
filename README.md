# Project_3_COVID



Project Proposal

Show the effects/spread of COVID-19 from 01/22/2020 - 07/27/2020

Create 3 Unique Views of the Data
 * Filter by Date drill down to country
    - Data Table of cases by Country
 * Roll-up total of deaths in a Bubble Chart
 * Bar Chart of spread over time


Requirements

  * Dashboard page with multiple charts that all reference the same data (Leaflet)
  * JavaScript Library not covered in class (chart.js)
  * House the data in a SQLite database
  * Create a Python Flask API
  * Includes a HTML/CSS
  * JavaScript, D3 
    

    This project was created to emphasize the importance of data keeping and organizing data for analysis. It also allowed us to learn and utilize different language platforms to merge data and create meaningful charts that interact with with the viewer making analyzation more understandable. With enough data, you can analyze different patterns and fluctuations in numbers. Included in this repository is COVID-19 data showing # of deaths, # of confirmed cases, and countries it affected from 1/22/2020-7/27/2020. The data was pulled from Kaggle into CSV files. These were then imported into Jupyter Notebook & explored through Pandas datagrams. A SQLite database was made through python and then a flask app was created to serve the API. A HTML file was created using Javascript, Leaflet, D3, Plotly, and chart.js to parse the data for creation into different graphs that show worldwide data in our dataset.

The Dashboard Page has been posted to the following github Page:
https://clangdon1023.github.io/Project_3_COVID/


Instructions to Open Files:

    *Download the file "Project_3_COVID" and git clone it to your desktop using your Gitbash(windows)/Terminal(mac).
    
    *Change Directory "cd" until you get to the file "Flask"
    
    *Run terminal/bash from "app.py"
    
    *After this runs, there will be an http web browser. Copy that and paste it into Google Chrome/Safari.
    
    *This will open up the flask program showing the the interactive dashboard.


Once the file is open, there is a drop down menu with dates ranging from 1/22/2020-7/27/2020. You can select any of these dates and see the graphs change between each selection. 

<img width="1184" alt="Global Recovered vs Active cases" src="https://github.com/clangdon1023/Project_3_COVID/assets/135924263/c938c680-421c-4468-8cb3-f463ccf4fa78">
[

<img width="714" alt="Screen Shot 2023-10-24 at 6 17 46 PM" src="https://github.com/clangdon1023/Project_3_COVID/assets/135924263/a3b17aed-ed43-4a61-8be0-c9d2fea676c4">


<img width="1327" alt="Screen Shot 2023-10-24 at 6 19 05 PM" src="https://github.com/clangdon1023/Project_3_COVID/assets/135924263/4b1833fc-cc04-482e-aa52-fb0a789b61b4">

Sources: 

[
](https://www.kaggle.com/datasets/imdevskp/corona-virus-report)]

[
](https://clangdon1023.github.io/Project_3_COVID/)
Project Credits: Clayton Langdon, Maxiel Liz, Samantha Barbey, Luke Pison, Aleksey Kozhokin, and Nikhil  

