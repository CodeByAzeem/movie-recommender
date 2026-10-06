import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=b1780acd77f1e4ad8d63b7bcf40f75f6&language=en-US")
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]

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
        movie_url = f"https://www.themoviedb.org/movie/{movie_id}"

        recommended_movie.append(movies.iloc[i[0]].title)
        recommended_movie_poster.append(fetch_poster(movie_id))
        recommended_movie_url.append(movie_url)

    return recommended_movie, recommended_movie_poster, recommended_movie_url

movies = pd.DataFrame(pickle.load(open('movies.pkl', 'rb')))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("🎬 Movie Recommender System")
st.subheader("Discover movies similar to your favorites! 🍿")

selected_movie_name = st.selectbox(
    'Which movie would you like recommendations for?',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters, url = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.markdown(
            f'''
            <a href="{url[0]}" target="_blank">
                <img src="{posters[0]}" width="200">
            </a>''',
            unsafe_allow_html=True)

    with col2:
        st.text(names[1])
        st.markdown(
            f'''
            <a href="{url[1]}" target="_blank">
                <img src="{posters[1]}" width="200">
            </a>''',
            unsafe_allow_html=True)

    with col3:
        st.text(names[2])
        st.markdown(
            f'''
            <a href="{url[2]}" target="_blank">
                <img src="{posters[2]}" width="200">
            </a>''',
            unsafe_allow_html=True)
        
    with col4:
        st.text(names[3])
        st.markdown(
            f'''
            <a href="{url[3]}" target="_blank">
                <img src="{posters[3]}" width="200">
            </a>''',
            unsafe_allow_html=True)
        
    with col5:
        st.text(names[4])
        st.markdown(
            f'''
            <a href="{url[4]}" target="_blank">
                <img src="{posters[4]}" width="200">
            </a>''',
            unsafe_allow_html=True)