
# 🎬 Movie Recommender System

A content-based Movie Recommender System built using Python and Streamlit. It recommends five movies similar to a user-selected movie and displays clickable movie posters fetched from The Movie Database (TMDB) API.

## 🚀 Features

- 🎥 **Movie Recommendations:** Recommends five similar movies based on the selected movie.
- 🔍 **Movie Selection:** Select a movie from an interactive dropdown menu.
- 🖼️ **Movie Posters:** Fetches movie posters using the TMDB API.
- 🔗 **Clickable Posters:** Click a poster to open the movie's TMDB page.
- ⚡ **Fast Recommendations:** Uses precomputed similarity scores for efficient recommendations.
- 🎨 **Custom UI:** Dark-themed interface with red accents and styled movie titles.
- 🌐 **Interactive Web App:** Simple and user-friendly interface built with Streamlit.

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
├── app.py                  # Streamlit application
├── models/
│   ├── movies.pkl          # Processed movie dataset
│   └── similarity.pkl      # Precomputed similarity matrix
├── requirements.txt        # Project dependencies
├── .gitignore              # Files excluded from Git
└── README.md               # Project documentation
```

## ⚙️ How It Works

This project uses **content-based filtering** to recommend movies based on similarity.

1. **Data Collection:** Movie information is collected from a movie dataset.
2. **Data Preprocessing:** Relevant movie information is cleaned and prepared.
3. **Feature Extraction:** Movie features are converted into numerical representations.
4. **Similarity Calculation:** Cosine similarity is used to measure similarity between movies.
5. **Recommendation:** When a user selects a movie, the system retrieves its similarity scores and recommends the five most similar movies.
6. **Poster Fetching:** The TMDB API retrieves posters for the recommended movies.

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

Get an API key from [The Movie Database (TMDB)](https://www.themoviedb.org/).

Create a file named `.streamlit/secrets.toml` in your project directory:

```toml
TMDB_API_KEY = "your_api_key_here"
```

The application accesses the key using Streamlit secrets:

```python
st.secrets["TMDB_API_KEY"]
```

**Important:** Never commit your actual API key to GitHub. Add `.streamlit/secrets.toml` to your `.gitignore` file.

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 👨‍💻 Author

**Azeem Ahmad**

- GitHub: [CodeByAzeem](https://github.com/CodeByAzeem)

## 📄 License

This project is intended for educational and portfolio purposes. Please review the licenses and terms of use for the datasets and APIs used before redistributing them.
