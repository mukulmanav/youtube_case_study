# YouTube Case Study

## 📌 Introduction
This project analyzes YouTube comments and video data using various Natural Language Processing (NLP) and Data Visualization techniques. The goal is to extract insights from user interactions, engagement metrics, and trending content.

## 📊 Analysis Performed

### 1️⃣ Sentiment Analysis
**Objective:** Determine the sentiment of YouTube comments.

**Methodology:**
- Sentiment polarity is measured on a scale from -1 to 1:
  - `-1` → Negative Sentiment
  - `0` → Neutral Sentiment
  - `1` → Positive Sentiment
- Added a polarity column to store sentiment scores for each comment.

### 2️⃣ WordCloud Analysis
**Objective:** Identify the most frequently used words in positive and negative comments.

**Methodology:**
- Created word clouds for positive and negative comments separately.
- Removed stop words (e.g., "is", "that", "the") to focus on meaningful words.

### 3️⃣ Emoji Analysis
**Objective:** Analyze emoji usage in YouTube comments.

**Methodology:**
- Extracted emojis from comment text.
- Counted the frequency of each emoji.
- Created a bar graph using Plotly to visualize emoji usage.

### 4️⃣ Most Liked Categories
**Objective:** Identify which YouTube categories receive the most likes.

**Methodology:**
- Collected video data from multiple countries.
- Merged all datasets into a single dataset.
- Created a boxplot to analyze the distribution of likes per category.

### 5️⃣ Engagement Analysis
**Objective:** Measure user engagement with videos.

**Methodology:**
- Calculated like rate, dislike rate, and comment count rate based on views.
- Analyzed correlation between views and engagement metrics.

### 6️⃣ Trending Channels
**Objective:** Identify the most trending YouTube channels.

**Methodology:**
- Grouped data by channel title.
- Counted the number of trending videos per channel.
- Created a barplot showing the top trending channels.

### 7️⃣ Impact of Punctuation on Views & Likes
**Objective:** Check if punctuation in video titles impacts engagement.

**Methodology:**
- Counted the number of punctuation marks in video titles.
- Created boxplots to analyze the relationship between punctuation count and views/likes.

## 📚 Libraries Used
The project utilizes the following Python libraries:

| Category | Libraries Used |
|----------|---------------|
| **Data Handling** | `pandas`, `numpy` |
| **Visualization** | `seaborn`, `matplotlib`, `plotly` |
| **NLP** | `textblob`, `wordcloud` |
| **Emoji Analysis** | `emoji`, `collections` |
| **Warnings** | `warnings` |


## 📌 Results & Insights
- Sentiment analysis shows that most comments are neutral, with a mix of positive and negative sentiments.
- WordClouds reveal common words and phrases used in positive and negative comments.
- Certain categories receive significantly more likes and engagement than others.
- Emojis play a crucial role in expressing emotions in comments.
- Channels with consistent content tend to have more trending videos.
- Punctuation in video titles does not significantly impact engagement metrics.

## 🏆 Conclusion
This project provides valuable insights into how users interact with YouTube videos through comments, likes, and engagement metrics. These findings can help content creators optimize their content strategy.

## 📌 Future Improvements
- Use Deep Learning models for more accurate sentiment classification.
- Implement topic modeling to categorize comments into meaningful themes.
- Perform time-series analysis on engagement metrics to detect trends over time.

## 📩 Contact
If you have any questions or suggestions, feel free to reach out!

✉️ Email: mukulmanav0@gmail.com

📌 GitHub: mukulmanav https://github.com/mukulmanav/youtube_case_study

🚀 **Happy Coding!** 🎉
