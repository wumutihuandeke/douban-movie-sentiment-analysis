# Douban Movie Review Sentiment Analysis

A Python-based natural language processing project for collecting and analyzing Chinese movie reviews from Douban.

## Project Overview

This project analyzes Chinese movie reviews using web data collection, text preprocessing, sentiment analysis, exploratory data analysis, and data visualization.

The project was developed as part of an undergraduate Big Data / Data Analysis course project.

Five movies were selected for analysis, with up to 500 short reviews collected for each movie.

## Objectives

The main objectives are to:

- Collect movie review data from Douban
- Extract review information including ratings, timestamps, and review content
- Process Chinese movie review text
- Perform sentiment classification using SnowNLP
- Analyze sentiment distributions
- Analyze frequently occurring words
- Examine monthly review volume trends
- Visualize the analysis results
- Export the processed data for further analysis

## Movies

The project analyzes reviews from five movies:

- 活着
- 霸王别姬
- 肖申克的救赎
- 泰坦尼克号
- 盗梦空间

Up to 500 reviews were collected for each movie.

## Technologies

- Python
- Requests
- BeautifulSoup
- Pandas
- jieba
- SnowNLP
- Matplotlib
- Seaborn
- WordCloud

## Methodology

### 1. Data Collection

Movie review data were collected from Douban using Python web scraping techniques.

The project uses:

- Requests for HTTP requests
- BeautifulSoup for HTML parsing

The following information is extracted from each review:

- Movie name
- Reviewer
- Rating
- Review time
- Review content

### 2. Text Processing

Chinese movie review text is processed using:

- Chinese word segmentation with jieba
- Basic text processing for word cloud generation

### 3. Sentiment Analysis

SnowNLP is used to calculate sentiment scores for Chinese movie reviews.

Reviews are classified into three categories according to the sentiment score:

- Positive: score > 0.6
- Neutral: 0.4 ≤ score ≤ 0.6
- Negative: score < 0.4

### 4. Exploratory Data Analysis

The project analyzes:

- Sentiment distribution
- Review ratings
- Frequently occurring words
- Monthly review volume
- Review time patterns

### 5. Visualization

The analysis results are visualized using:

- Matplotlib
- Seaborn
- WordCloud

The project generates:

- Sentiment distribution chart
- Word cloud
- Monthly review volume trend chart

### 6. Data Export

The processed analysis results are exported to an Excel file for further analysis.

## Project Structure

```text
douban-movie-sentiment-analysis/
│
├── README.md
├── douban_movie_sentiment_analysis.py
├── requirements.txt
├── .gitignore
└── LICENSE

## Output

The project generates the following analysis results:

- `情感分布.png`
- `词云图.png`
- `评论趋势.png`
- `豆瓣电影短评分析结果.xlsx`

## Learning Outcomes

Through this project, I gained practical experience in:

- Web data collection
- HTML parsing
- Chinese text processing
- Natural language processing
- Sentiment analysis
- Exploratory data analysis
- Data visualization
- Data export and organization

## Academic Context

This project was completed as an undergraduate course project related to Big Data and Data Analysis.
