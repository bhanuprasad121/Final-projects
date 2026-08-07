# 🎾 Tennis Game Analytics using Sportradar API

## 📌 Project Overview

This project is a complete Tennis Game Analytics solution developed using the Sportradar Tennis API. It extracts tennis competition, venue, and competitor ranking data from the API, transforms nested JSON into a relational format, stores the data in a MySQL database, and provides an interactive Streamlit dashboard for analysis and visualization.

The application enables users to explore competitions, venues, competitor rankings, country-wise statistics, and leaderboards through an easy-to-use interface.

---

## 🎯 Objectives

- Extract tennis data from the Sportradar API.
- Transform nested JSON into relational tables.
- Store the processed data in MySQL.
- Execute SQL queries for analytical insights.
- Build an interactive Streamlit dashboard.
- Visualize tennis competitions and competitor rankings.

---

## 🛠️ Technologies Used

- Python 3.x
- Pandas
- Requests
- SQLAlchemy
- MySQL
- Streamlit
- Sportradar Tennis API
- Git & GitHub

---

## 📂 Project Structure

```
Tennis_Game_Analytics/
│
├── api/
│   ├── api_config.py
│   ├── extract_competitions.py
│   ├── extract_complexes.py
│   └── extract_rankings.py
│
├── transform/
│   ├── transform_competitions.py
│   ├── transform_complexes.py
│   └── transform_rankings.py
│
├── database/
│   ├── create_tables.sql
│   ├── analysis_queries.sql
│   ├── db_connection.py
│   └── load_data.py
│
├── streamlit_app/
│   └── app.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│
├── requirements.txt
├── README.md
├── .gitignore
└── main.py
```

---

## 📊 Database Schema

The project stores data in six relational tables:

- Categories
- Competitions
- Complexes
- Venues
- Competitors
- Competitor Rankings

Relationships are maintained using Primary Keys and Foreign Keys.

---

## 📈 Features

### Home Dashboard

- Total Competitors
- Countries Represented
- Highest Ranking Points
- Leaderboard

### Competitor Search

- Search competitors by name
- Filter by country
- Filter by rank
- Filter by points

### Competitor Details

Displays:

- Name
- Country
- Rank
- Ranking Movement
- Competitions Played
- Points

### Country Analysis

- Number of competitors by country
- Average ranking points

### Leaderboards

- Top Ranked Competitors
- Highest Points Scored

---

## 📋 SQL Analysis

The project includes SQL queries for:

### Competition Analysis

- List competitions with categories
- Count competitions by category
- Doubles competitions
- Parent and child competitions
- Competition type distribution

### Venue Analysis

- Venues with complexes
- Venues by country
- Venues by timezone
- Complexes containing multiple venues

### Competitor Analysis

- Competitor rankings
- Top 5 competitors
- Stable rankings
- Points by country
- Competitor count by country
- Highest scoring competitors

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Tennis_Game_Analytics.git

cd Tennis_Game_Analytics
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
SPORTRADAR_API_KEY=YOUR_API_KEY

DB_USER=root
DB_PASSWORD=YOUR_PASSWORD
DB_HOST=localhost
DB_NAME=tennis_analytics
```

---

## 🗄️ Database Setup

Create the database:

```sql
CREATE DATABASE tennis_analytics;
```

Execute:

```
database/create_tables.sql
```

---

## ▶️ Run the Project

### Extract API Data

```bash
python -m api.extract_competitions

python -m api.extract_complexes

python -m api.extract_rankings
```

### Transform Data

```bash
python -m transform.transform_competitions

python -m transform.transform_complexes

python -m transform.transform_rankings
```

### Load Data into MySQL

```bash
python -m database.load_data
```

### Launch Streamlit

```bash
streamlit run streamlit_app/app.py
```

---

## 📷 Screenshots

Include screenshots of:

- Home Dashboard
- Competitor Search
- Competitor Details
- Country Analysis
- Leaderboards

---

## 📁 Deliverables

- Python Scripts
- SQL Database Schema
- SQL Analysis Queries
- Streamlit Application
- README Documentation

---

## 👤 Author

**Pujari Bhanu Prasad**

---

## 📜 License

This project is developed for educational purposes as part of a Data Analytics assignment.
