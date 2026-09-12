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

# Calculate similarity between all songs
similarity = cosine_similarity(feature_matrix)


def recommend_songs(song_name, number_of_recommendations=5):
    # Remove extra spaces and make the search case-insensitive
    song_name = song_name.strip().lower()

    matches = songs[songs["song"].str.lower() == song_name]

    if matches.empty:
        print("\nSong not found.")
        print("Please enter a song name from the dataset.")
        return

    song_index = matches.index[0]

    # Get similarity scores for the selected song
    similarity_scores = list(enumerate(similarity[song_index]))

    # Sort by similarity score
    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    print(f"\nRecommendations for: {songs.iloc[song_index]['song']}")
    print("-" * 50)

    count = 0

    for index, score in similarity_scores:

        # Don't recommend the same song
        if index == song_index:
            continue

        song = songs.iloc[index]

        print(
            f"{count + 1}. {song['song']} - {song['artist']} "
            f"({song['genre']})"
        )

        count += 1

        if count == number_of_recommendations:
            break


# Get input from the user
song_name = input("Enter a song name: ")

recommend_songs(song_name)