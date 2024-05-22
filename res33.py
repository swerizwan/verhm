import librosa
import os
import pandas as pd
import plotly.express as px
import plotly.io as pio

# Set up the directory containing audio files
RAV = 'ravdessdataset/audio_speech_actors_01-24/'
dir_list = os.listdir(RAV)

# Initialize lists to store data
emotion = []
gender = []
path = []

# Iterate through directories and files to collect data
for i in dir_list:
    fname = os.listdir(RAV + i)
    for f in fname:
        part = f.split('.')[0].split('-')
        # Extract emotion and gender from the file name
        emotion.append(int(part[2]))
        temp = int(part[6])
        gender.append("female" if temp % 2 == 0 else "male")
        # Store the file path
        path.append(RAV + i + '/' + f)

# Encode emotion labels
emotion_labels = {1: 'neutral', 2: 'neutral', 3: 'happy', 4: 'sad', 5: 'angry', 6: 'fear', 7: 'disgust', 8: 'surprise'}
emotion = [emotion_labels[e] for e in emotion]

# Create DataFrame
RAV_df = pd.DataFrame({'gender': gender, 'emotion': emotion, 'path': path})

# Combine gender and emotion to form labels
RAV_df['labels'] = RAV_df['gender'] + '_' + RAV_df['emotion']
RAV_df['source'] = 'RAVDESS'

# Prepare visualizations
# Emotion Count
import matplotlib.pyplot as plt

# Emotion Count
emotion_count = RAV_df['emotion'].value_counts().sort_index()
plt.bar(emotion_count.index, emotion_count.values, color='skyblue')
plt.title('Emotion Count of Each Emotion Category in RAVDESS Dataset')
plt.xlabel('Emotion Categories')
plt.ylabel('Count')
plt.xticks(emotion_count.index)
# plt.grid(axis='y')
plt.savefig('ravdess_emotion_count.svg')
plt.show()

# Label Count
label_count = RAV_df['labels'].value_counts().sort_index()
plt.bar(range(len(label_count)), label_count.values, color='orange')
plt.title('Label Count of Each Emotion Category in RAVDESS Dataset')
plt.xlabel('Label')
plt.ylabel('Count')
plt.xticks(range(len(label_count)), label_count.index, rotation=45, ha='right')
# plt.grid(axis='y')
plt.tight_layout()
plt.savefig('ravdess_label_count.svg')
plt.show()

