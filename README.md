
# 🎬 Movie Recommender System

A content-based Movie Recommender System built using Python and Streamlit. The application recommends movies similar to a movie selected by the user and displays movie posters using The Movie Database (TMDB) API.

## 🚀 Features

- 🎥 **Movie Recommendations:** Recommends 5 similar movies based on the selected movie.
- 🔍 **Movie Selection:** Search and select movies from a dropdown menu.
- 🖼️ **Movie Posters:** Fetches movie posters using the TMDB API.
- 🔗 **Clickable Posters:** Click on a movie poster to open its TMDB page.
- ⚡ **Fast Recommendations:** Uses precomputed similarity scores for efficient recommendations.
- 🌐 **Interactive Web App:** Built with Streamlit for a simple and user-friendly interface.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Requests
- Pickle
- TMDB API

## 📂 Project Structure

```text
movie-recommender/
│
├── app.py                 # Streamlit application
├── movies.pkl             # Processed movie dataset
├── similarity.pkl         # Precomputed similarity matrix
├── requirements.txt       # Project dependencies
├── .gitignore             # Files excluded from Git
└── README.md              # Project documentation
```

## ⚙️ How It Works

This project uses content-based filtering to recommend movies.

1. **Data Collection:** Movie information is collected from a movie dataset.
2. **Data Preprocessing:** Relevant movie information is cleaned and transformed into features.
3. **Feature Extraction:** Movie features are converted into numerical representations.
4. **Similarity Calculation:** Cosine similarity is used to calculate similarity scores between movies.
5. **Recommendation:** When a user selects a movie, the system retrieves its similarity scores and recommends the five most similar movies.
6. **Poster Fetching:** The TMDB API retrieves movie posters for the recommended movies.

## 📥 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/CodeByAzeem/movie-recommender.git
```

### 2. Navigate to the Project Directory

```bash
cd movie-recommender
```

### 3. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the TMDB API Key

Create an API key through [The Movie Database (TMDB)](https://www.themoviedb.org/).

For example, create `.streamlit/secrets.toml`:

```toml
TMDB_API_KEY = "your_api_key_here"
```

Access it in Streamlit using:

```python
api_key = st.secrets["TMDB_API_KEY"]
```

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 👨‍💻 Author

**Azeem Ahmad**

- GitHub: https://github.com/CodeByAzeem

## 📄 License

This project is intended for educational and portfolio purposes. Review the licenses and terms of use of the datasets and APIs used before redistributing them.
