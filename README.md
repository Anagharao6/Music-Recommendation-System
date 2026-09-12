# 🎵 Music Recommendation System

A content-based music recommendation system built using **Python, Pandas, Scikit-learn, and Streamlit**.

The system recommends songs that are musically similar to a selected song using audio-related features such as **danceability, energy, acousticness, and valence**.

## 🚀 Features

* 🎵 Select a song from the available dataset
* 🔎 Find similar songs using cosine similarity
* 📊 Scale numerical features using StandardScaler
* 🎯 Choose the number of recommendations
* 🌐 Interactive Streamlit web interface
* 💻 Command-line recommendation version

## 🧠 How It Works

The system follows these steps:

1. Loads the song dataset using Pandas.
2. Selects important numerical music features.
3. Scales the features using `StandardScaler`.
4. Calculates similarity between songs using **cosine similarity**.
5. Finds the songs most similar to the selected song.
6. Displays the recommendations through a Streamlit web interface.

### Features Used

* **Danceability** – How suitable a song is for dancing.
* **Energy** – The intensity and activity level of the song.
* **Acousticness** – How strongly the song resembles acoustic music.
* **Valence** – The musical positivity or mood of the song.

## 🖥️ Web Application

The project includes an interactive Streamlit interface where users can:

1. Select a song.
2. Choose the number of recommendations.
3. Click **Recommend Songs**.
4. View recommended songs along with their artists, genres, and similarity scores.

## 📁 Project Structure

```text
Music-Recommendation-System/
│
├── data/
│   └── songs.csv
│
├── app.py
├── recommend.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit
* Git
* GitHub

## 📊 Dataset

The dataset contains information about songs and their musical characteristics.

| Column       | Description              |
| ------------ | ------------------------ |
| song         | Song name                |
| artist       | Artist name              |
| genre        | Music genre              |
| danceability | Danceability score       |
| energy       | Energy score             |
| acousticness | Acousticness score       |
| valence      | Musical positivity score |

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Anagharao6/Music-Recommendation-System.git
```

### 2. Open the project folder

```bash
cd Music-Recommendation-System
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

## 💻 Command-Line Version

The recommendation system can also be run directly from the terminal:

```bash
python recommend.py
```

Enter a song name when prompted to receive recommendations.

## 🔮 Future Improvements

* Use a larger real-world music dataset.
* Add more audio features.
* Include album artwork and song previews.
* Add genre and artist filtering.
* Improve the recommendation algorithm using additional machine learning techniques.
* Deploy the Streamlit application online.

## 🎯 Project Objective

The objective of this project is to demonstrate how **machine learning-based similarity techniques** can be used to build a simple personalized music recommendation system.
