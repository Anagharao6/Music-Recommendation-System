# Music Recommendation System

A content-based music recommendation system built using Python, Pandas, and Scikit-learn. The system recommends songs that are similar to a selected song based on its audio features.

## How It Works

The system uses four audio-related features:

* Danceability
* Energy
* Acousticness
* Valence

The feature values are first standardized using `StandardScaler`. The system then calculates the similarity between songs using **cosine similarity**.

When a user enters a song name, the system finds songs with the most similar feature patterns and displays the top recommendations.

## Example

```text
Enter a song name: Believer

Recommendations for: Believer
--------------------------------------------------
1. Don't Start Now - Dua Lipa (Pop)
2. Levitating - Dua Lipa (Pop)
3. On My Way - Alan Walker (Electronic)
4. Demons - Imagine Dragons (Rock)
5. Counting Stars - OneRepublic (Pop Rock)
```

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Cosine Similarity
* StandardScaler

## Project Structure

```text
Music-Recommendation-System/
│
├── data/
│   └── songs.csv
│
├── recommend.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Dataset

The project uses a sample dataset containing:

* Song name
* Artist
* Genre
* Danceability
* Energy
* Acousticness
* Valence

## How to Run

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

### 4. Run the recommendation system

```bash
python recommend.py
```

### 5. Enter a song name

For example:

```text
Believer
```

## Future Improvements

* Add a larger music dataset
* Add more audio features
* Build a graphical or web-based interface
* Allow users to select the number of recommendations
* Improve recommendations using additional machine learning techniques

## Project Objective

The objective of this project is to demonstrate how similarity-based recommendation can be used to suggest songs with similar characteristics based on numerical audio features.
