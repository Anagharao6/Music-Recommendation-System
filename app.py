import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity


# Load dataset
songs = pd.read_csv("data/songs.csv")

# Features used for recommendation
features = [
    "danceability",
    "energy",
    "acousticness",
    "valence"
]

# Scale features
scaler = StandardScaler()
feature_matrix = scaler.fit_transform(songs[features])

# Calculate similarity
similarity = cosine_similarity(feature_matrix)


# Page title
st.title("🎵 Music Recommendation System")

st.write(
    "Select a song to get recommendations based on its musical features."
)


# Song selection
song_name = st.selectbox(
    "Choose a song:",
    songs["song"].tolist()
)


# Number of recommendations
number_of_recommendations = st.slider(
    "Number of recommendations:",
    min_value=1,
    max_value=10,
    value=5
)


# Recommendation button
if st.button("Recommend Songs"):

    song_index = songs[
        songs["song"] == song_name
    ].index[0]

    similarity_scores = list(
        enumerate(similarity[song_index])
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for index, score in similarity_scores:

        if index == song_index:
            continue

        song = songs.iloc[index]

        recommendations.append({
            "Song": song["song"],
            "Artist": song["artist"],
            "Genre": song["genre"],
            "Similarity Score": round(score, 3)
        })

        if len(recommendations) == number_of_recommendations:
            break

    st.subheader(f"Recommendations for: {song_name}")

    st.dataframe(
        pd.DataFrame(recommendations),
        use_container_width=True
    )