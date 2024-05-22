# Voice-Driven 3D Facial Emotion Recognition For Mental Health Monitoring

## About the Project

Vocal expressions are significant indicators of emotional states, crucial for mental health monitoring. However, existing methods often struggle to accurately separate the emotions and contents conveyed through speech alone. Our solution introduces a neural network that effectively disentangles various emotions from voice signals, enabling the generation of precise 3D facial expressions.

## Workflow

To begin, ensure you have the following essential libraries installed on your system:

- Pytorch 1.9.0
- CUDA 11.3
- Blender 3.4.1
- ffmpeg 4.4.1
- torch==1.9.0
- torchvision==0.10.0
- torchaudio==0.9.0
- numpy
- scipy==1.7.1
- librosa==0.8.1
- tqdm
- pickle
- transformers==4.6.1
- trimesh==3.9.27
- pyrender==0.1.45
- opencv-python

## Installation

Follow these steps to set up the project:

1. Download the repository.
2. Create a conda virtual environment using: `conda create -n verhm python=3.7`.
3. Activate the environment: `conda activate verhm`.
4. Install all required dependencies mentioned in the Workflow section.
   
## Datasets

Our project utilizes several datasets for training and testing purposes:

- **VOCASET**: Offers audio-4D scan pairs for emotion analysis. [Dataset Link](https://voca.is.tue.mpg.de/download.php)
- **RAVDESS**: The RAVDESS comprises 7,356 files, totaling 24.8 GB in size. It features recordings from 24 professional actors, evenly split between genders. [Dataset Link](https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio)
- **MEAD**: The MEAD \cite{Mead} features 60 actors and actresses conversing with eight distinct emotions at varying intensity levels. [Dataset Link](https://wywu.github.io/projects/MEAD/MEAD.html/)
