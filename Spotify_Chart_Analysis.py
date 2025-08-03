# Spotify Chart Analysis
# Author: Andrew Hashoush

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("/Users/andrewhashoush/Downloads/charts.csv")  

# Preview data
print(df.head())
print(df.columns)

# Convert 'date' to datetime
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year

# -------------------------------
# Top 10 Most Streamed Songs
# -------------------------------
top_tracks = df.groupby('title')['streams'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_tracks.values, y=top_tracks.index, palette='crest')
plt.title('Top 10 Most Streamed Songs (All Time)')
plt.xlabel('Total Streams')
plt.ylabel('Song Title')
plt.tight_layout()
plt.show()

# -------------------------------
# Average Streams per Year
# -------------------------------
yearly_streams = df.groupby('year')['streams'].mean().reset_index()

plt.figure(figsize=(10, 5))
sns.lineplot(data=yearly_streams, x='year', y='streams')
plt.title('Average Daily Streams by Year')
plt.xlabel('Year')
plt.ylabel('Avg Streams per Song')
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------------------
# Top 5 Streaming Countries
# -------------------------------
top_countries = df.groupby('region')['streams'].sum().sort_values(ascending=False).head(5)

plt.figure(figsize=(8, 5))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='mako')
plt.title('Top 5 Countries by Total Streams')
plt.xlabel('Total Streams')
plt.ylabel('Country')
plt.tight_layout()
plt.show()

# -------------------------------
# Most Featured Artists
# -------------------------------
top_artists = df['artist'].value_counts().head(10)

plt.figure(figsize=(10, 5))
sns.barplot(x=top_artists.values, y=top_artists.index, palette='plasma')
plt.title('Top 10 Most Frequently Charting Artists')
plt.xlabel('Number of Chart Appearances')
plt.ylabel('Artist')
plt.tight_layout()
plt.show()

# -------------------------------
# Stream Trend Breakdown
# -------------------------------
trend_counts = df['trend'].value_counts().head(5)

plt.figure(figsize=(6, 6))
plt.pie(trend_counts, labels=trend_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Stream Position Change Trends')
plt.tight_layout()
plt.show()
