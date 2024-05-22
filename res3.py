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
emotion_count_fig = px.histogram(RAV_df, x='emotion', color='emotion',  
                      title='Emotion Count of Each Emotion Category in RAVDESS Dataset')
emotion_count_fig.update_layout(bargap=0.2)
pio.write_image(emotion_count_fig, 'emotion_count.svg')
emotion_count_fig.show()

# Label Count
label_count_fig = px.histogram(RAV_df, x='labels', color='emotion',  
                      title='Label Count of Each Emotion Category in RAVDESS Dataset')
label_count_fig.update_layout(bargap=0.2)
pio.write_image(label_count_fig, 'label_count.svg')
label_count_fig.show()
