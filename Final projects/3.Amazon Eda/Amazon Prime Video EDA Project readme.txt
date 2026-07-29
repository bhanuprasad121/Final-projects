Amazon Prime Video EDA Project
📌 Project Overview

This project performs an Exploratory Data Analysis (EDA) on the Amazon Prime Video dataset to understand the platform's content library. The analysis explores content distribution, genres, release trends, production countries, ratings, runtime, and the contributions of directors and actors. The objective is to uncover meaningful insights that can support content strategy and business decision-making.

🎯 Business Objective

The main objective of this project is to analyze Amazon Prime Video's content catalog to identify trends in content production, audience ratings, genres, and regional distribution. The insights can help improve content acquisition, recommendation systems, and strategic planning.

📂 Dataset Information
Titles Dataset
Column	Description
id	Unique identifier for each title
title	Name of the movie or TV show
type	Content type (Movie or Show)
description	Brief description of the title
release_year	Year the content was released
age_certification	Age rating (e.g., PG-13, TV-MA)
runtime	Duration in minutes
genres	Genre(s) of the content
production_countries	Country/Countries where the content was produced
seasons	Number of seasons (for TV shows)
imdb_id	IMDb unique identifier
imdb_score	IMDb rating
imdb_votes	Number of IMDb votes
tmdb_popularity	TMDb popularity score
tmdb_score	TMDb rating
Credits Dataset
Column	Description
person_id	Unique identifier for cast/crew member
id	Title identifier
name	Name of actor/director
character	Character played
role	Role (Actor/Director)
🛠 Tools & Libraries
Python
Pandas
NumPy
Matplotlib
Seaborn
Google Colab / Jupyter Notebook
📊 Data Cleaning

The following preprocessing steps were performed:

Removed duplicate records.
Checked and handled missing values.
Cleaned text columns.
Converted release year into a usable format.
Processed genres and production countries for analysis.
Standardized categorical values.
📈 Exploratory Data Analysis

The following analyses were performed:

Content distribution (Movies vs TV Shows)
Content releases over the years
Genre distribution
Age certification distribution
Top production countries
Top credited directors
Top frequent actors
Runtime distribution
IMDb and TMDb rating analysis
Correlation Heatmap
Pair Plot
Genre-wise release heatmap
Time-series analysis of content releases
🔍 Key Insights
Movies make up the majority of the content library.
Drama is the most common genre, followed by Comedy.
The United States contributes the highest number of titles, followed by India and the United Kingdom.
Content production increased significantly after 2010.
IMDb Score and TMDb Score show a moderate positive correlation.
Movies generally have longer runtimes than TV Shows.
A few directors and actors contribute a large number of titles.
💼 Business Recommendations
Continue investing in high-performing genres such as Drama and Comedy.
Expand regional content to attract a wider international audience.
Strengthen collaborations with frequently credited directors and actors.
Use audience ratings and popularity metrics to improve content recommendations.
Increase investment in quality TV Shows to support binge-watching trends.
✅ Conclusion

The exploratory data analysis provides valuable insights into Amazon Prime Video's content library. The findings show strong growth in content production, dominance of movies over TV shows, and the popularity of genres such as Drama and Comedy. By leveraging these insights, Amazon Prime Video can make informed decisions regarding content acquisition, production, and recommendation strategies, ultimately improving viewer engagement and subscriber satisfaction.

👨‍💻 Author

Pujari Bhanu Prasad
Project: Amazon Prime Video Exploratory Data Analysis (EDA)
Tools Used: Python, Pandas, NumPy, Matplotlib, Seaborn, Jupyter Notebook