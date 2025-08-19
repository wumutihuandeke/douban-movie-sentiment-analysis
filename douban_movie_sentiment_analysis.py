import requests
from bs4 import BeautifulSoup
import pandas as pd
import jieba
from snownlp import SnowNLP
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
import time
import os
import matplotlib
matplotlib.rcParams['font.family'] = 'Microsoft YaHei'


HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

# 电影及其对应链接
MOVIES = {
    "活着": "https://movie.douban.com/subject/1292365/comments",
    "霸王别姬": "https://movie.douban.com/subject/1291546/comments",
    "肖申克的救赎": "https://movie.douban.com/subject/1292052/comments",
    "泰坦尼克号": "https://movie.douban.com/subject/1292722/comments",
    "盗梦空间": "https://movie.douban.com/subject/3541415/comments"
}

def get_comments(url, max_comments=500):
    comments = []
    start = 0
    while len(comments) < max_comments:
        params = {'start': start, 'limit': 20, 'status': 'P'}
        res = requests.get(url, headers=HEADERS, params=params)
        soup = BeautifulSoup(res.text, 'html.parser')
        comment_list = soup.find_all('div', class_='comment')
        if not comment_list:
            break
        for comment in comment_list:
            user = comment.find('span', class_='comment-info').find('a').text.strip()
            rating_span = comment.find('span', class_='rating')
            rating = 0
            if rating_span:
                rating_class = rating_span['class'][0]
                try:
                    rating = int(rating_class.replace('allstar', '')) // 10
                except:
                    rating = 0
            time_str = comment.find('span', class_='comment-time')['title']
            content = comment.find('span', class_='short').text.strip()
            comments.append([user, rating, time_str, content])
            if len(comments) >= max_comments:
                break
        start += 20
        time.sleep(0.5)
    return comments

def sentiment_label(text):
    s = SnowNLP(text)
    score = s.sentiments
    if score > 0.6:
        return '正面'
    elif score < 0.4:
        return '负面'
    else:
        return '中性'

def analyze(df_all):
    df_all['情感'] = df_all['短评信息'].apply(sentiment_label)
    print("情感分布：\n", df_all['情感'].value_counts())

    plt.figure(figsize=(8, 5))
    sns.countplot(x='情感', data=df_all, order=['正面', '中性', '负面'], palette='Set2')
    plt.title('情感分布')
    plt.savefig('情感分布.png')
    plt.show()

    # 词云
    text = ' '.join(df_all['短评信息'])
    word_list = list(jieba.cut(text))
    if word_list:
        wordcloud = WordCloud(font_path='C:/Windows/Fonts/msyh.ttc', width=800, height=400, background_color='white').generate(' '.join(word_list))
        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('词云图')
        plt.savefig('词云图.png')
        plt.show()
    else:
        print("词云跳过：无有效分词")

    # 时间趋势
    df_all['评论时间'] = pd.to_datetime(df_all['评论时间'], errors='coerce')
    df_all = df_all.dropna(subset=['评论时间'])
    df_all.set_index('评论时间', inplace=True)
    monthly_counts = df_all.resample('M').size()

    plt.figure(figsize=(10, 5))
    monthly_counts.plot()
    plt.title('每月评论数量趋势')
    plt.xlabel('时间')
    plt.ylabel('评论数')
    plt.savefig('评论趋势.png')
    plt.show()

    df_all.to_excel('豆瓣电影短评分析结果.xlsx', index=False)

    print("分析完成：已保存Excel和图像文件")

if __name__ == "__main__":
    all_comments = []
    for name, url in MOVIES.items():
        print(f"抓取：{name}")
        data = get_comments(url, max_comments=500)
        for d in data:
            all_comments.append([name] + d)
    df = pd.DataFrame(all_comments, columns=['电影名', '评论人', '评分', '评论时间', '短评信息'])
    analyze(df)
