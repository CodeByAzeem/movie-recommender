import streamlit as st
import pickle
import pandas as pd
import requests

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #141414;
    color: white;
}

h1 {
    text-align: center;
    color: #E50914;
}

h3 {
    text-align: center;
    color: white;
}

div.stButton > button {
    background-color: #E50914;
    color: white;
    border-radius: 8px;
    border: none;
    height: 45px;
    font-weight: bold;
}

div.stButton > button:hover {
    background-color: #b20710;
    color: white;
}

</style>
""", unsafe_allow_html=True)

def load_data():
    with open("models/movies.pkl", "rb") as f:
        movies = pickle.load(f)

    with open("models/similarity.pkl", "rb") as f:
        similarity = pickle.load(f)

    movies = movies.reset_index(drop=True)

    return movies, similarity

movies, similarity = load_data()

def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={st.secrets['TMDB_API_KEY']}&language=en-US")
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]

    distance = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distance)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movie = []
    recommended_movie_poster = []
    recommended_movie_url = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movie.append(movies.iloc[i[0]].title)
        recommended_movie_poster.append(fetch_poster(movie_id))
        recommended_movie_url.append(
            f"https://www.themoviedb.org/movie/{movie_id}"
        )

    return recommended_movie, recommended_movie_poster, recommended_movie_url

st.title("🎬 Movie Recommender System")
st.markdown(
    "<h3>Discover movies similar to your favorites 🍿</h3>",
    unsafe_allow_html=True
)

st.write("")

selected_movie_name = st.selectbox(
    "Choose a movie",
    movies["title"].values
)

if st.button("Recommend Movies", use_container_width=True):

    names, posters, urls = recommend(selected_movie_name)

    st.subheader("🍿 Recommended For You")

    columns = st.columns(5)

    for i in range(5):
        with columns[i]:

            if posters[i]:
                st.markdown(
                    f"""
                    <a href="{urls[i]}" target="_blank">
                        <img src="{posters[i]}"
                             style="width:100%; border-radius:10px;">
                    </a>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.write("Poster unavailable")

            st.markdown(
                f"""
                <p style="
                    text-align: center;
                    color: white;
                    font-size: 16px;
                    font-weight: bold;
                    margin-top: 10px;
                ">
                    {names[i]}
                </p>
                """,
                unsafe_allow_html=True
            )

st.markdown("---")
st.caption("Made with ❤️ using Python and Streamlit")