# Douban Movie Review Sentiment Analysis

A Python-based natural language processing project for analyzing the sentiment of Chinese movie reviews collected from Douban.

## Project Overview

This project explores sentiment patterns in Chinese movie reviews using web data collection, text preprocessing, sentiment analysis, and data visualization.

The project was developed as part of an undergraduate Big Data / Data Analysis course project.

## Objectives

The main objectives are to:

- Collect movie review data from Douban
- Clean and preprocess Chinese text
- Perform sentiment analysis on user reviews
- Analyze sentiment distributions and trends
- Identify frequently discussed topics
- Visualize the results

## Technologies

- Python
- Requests
- BeautifulSoup
- Pandas
- NumPy
- jieba
- SnowNLP
- Matplotlib
- Seaborn
- WordCloud

## Methodology

### 1. Data Collection

Movie review data were collected using Python-based web scraping techniques.

The project used:

- Requests
- BeautifulSoup

to retrieve and parse review information.

### 2. Text Preprocessing

Chinese review text was processed using:

- Text cleaning
- Chinese word segmentation with jieba
- Removal of unnecessary characters and content

### 3. Sentiment Analysis

SnowNLP was used to calculate sentiment scores for Chinese movie reviews.

Reviews were subsequently analyzed according to their sentiment scores.

### 4. Exploratory Data Analysis

The project analyzes:

- Sentiment distribution
- Frequently occurring words
- Review characteristics
- Sentiment trends

### 5. Visualization

The analysis results were visualized using:

- Matplotlib
- Seaborn
- WordCloud

## Project Structure

```text
douban-movie-sentiment-analysis/
│
├── README.md
├── douban_movie_sentiment_analysis.py
├── requirements.txt
├── .gitignore
└── LICENSE
