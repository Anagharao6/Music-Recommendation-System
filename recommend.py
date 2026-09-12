import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
songs = pd.read_csv("data/songs.csv")

# Features used for recommendation
features = [
    "danceability",
    "energy",
    "acousticness",
    "valence"
]

# Scale the numerical features
scaler = StandardScaler()
feature_matrix = scaler.fit_transform(songs[features])

# Calculate similarity between songs
similarity = cosine_similarity(feature_matrix)


def recommend_songs(song_name, number_of_recommendations=5):
    # Find the selected song
    matches = songs[songs["song"].str.lower() == song_name.lower()]

    if matches.empty:
        print("Song not found.")
        return

    song_index = matches.index[0]

    # Get similarity scores for the selected song
    similarity_scores = list(enumerate(similarity[song_index]))

    # Sort from most similar to least similar
    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    print("\nRecommended songs:")

    count = 0

    for index, score in similarity_scores:
        if index == song_index:
            continue

        print(
            f"{count + 1}. {songs.iloc[index]['song']} "
            f"- {songs.iloc[index]['artist']}"
        )

        count += 1

        if count == number_of_recommendations:
            break


# Get song name from the user
song_name = input("Enter a song name: ")

recommend_songs(song_name)