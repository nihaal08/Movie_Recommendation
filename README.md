Here's a polished and professional `README.md` file for your **Movie Recommendation System** project, formatted for clarity, readability, and appeal on platforms like GitHub:

---

# 🎬 Movie Recommendation System

A content-based movie recommendation engine that uses **NLP techniques** and **cosine similarity** to suggest movies similar to a user-selected title. Built with **Streamlit**, this interactive dashboard enables users to explore and discover new movies in a visually engaging manner.

---

## 📌 Project Overview

This project is a content-based filtering system that analyzes movie metadata (genres, keywords, cast, crew, and overviews) to recommend similar movies. It is powered by data from the **TMDB 5000 Movie Dataset** and includes two key components:

* 🧠 **Model Building** (`movie.ipynb`): Preprocesses data, builds the recommendation engine, and saves artifacts.
* 🌐 **Web Application** (`movie.py`): Streamlit-based interface that fetches and displays recommendations and movie posters using the TMDB API.

---

## ✨ Features

* 🎯 **Content-Based Filtering**: Recommends movies based on shared features like cast, crew, genres, and descriptions.
* 🖼️ **Poster Display**: Integrates the TMDB API to fetch and show movie posters dynamically.
* ⚡ **Efficient Preprocessing**: Includes JSON parsing, feature engineering, and vectorization.
* 📊 **Interactive Dashboard**: Built using **Streamlit**, users can search and explore recommendations easily.
* 📈 **Scalable Model**: Uses cosine similarity for accurate, fast results.

---

## 📁 Dataset

* **Source**: [TMDB 5000 Movie Dataset on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
* **Files Used**:

  * `tmdb_5000_movies.csv`
  * `tmdb_5000_credits.csv`
* **Metadata Includes**:

  * Movie titles and IDs
  * Overviews and keywords
  * Genres, cast, and crew details

---

## 🗂️ Project Structure

```
movie-recommendation-system/
│
├── movie.ipynb              # Data preprocessing and model building
├── movie.py                 # Streamlit application
├── movies_data.pkl          # Processed movie data
├── similarity_matrix.pkl    # Cosine similarity matrix
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## ⚙️ Installation

### 📌 Prerequisites

* Python 3.8+
* Jupyter Notebook
* Streamlit
* TMDB API Key

### 🔧 Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd movie-recommendation-system
   ```

2. **Create Virtual Environment & Install Dependencies**

   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate

   pip install -r requirements.txt
   ```

   **`requirements.txt`:**

   ```
   numpy
   pandas
   scikit-learn
   streamlit
   requests
   ```

3. **Download the Dataset**

   * Download from Kaggle and place both:

     * `tmdb_5000_movies.csv`
     * `tmdb_5000_credits.csv`
   * into the root directory.

4. **Get TMDB API Key**

   * Sign up at [TMDB](https://www.themoviedb.org/) and get your API key.
   * Replace `<your-api-key>` in `movie.py`:

     ```python
     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=<your-api-key>&language=en-US"
     ```

---

## 🚀 Running the Project

### 1. Preprocess & Build Model

```bash
jupyter notebook movie.ipynb
```

* Run all cells to generate:

  * `movies_data.pkl`
  * `similarity_matrix.pkl`

### 2. Launch Streamlit App

```bash
streamlit run movie.py
```

* Open your browser and go to: [http://localhost:8501](http://localhost:8501)

---

## 🧠 Usage

1. **Select a Movie**: Use the dropdown in the sidebar.
2. **Click 'Get Recommendations'**.
3. **View Results**: Top 5 similar movies displayed with titles and posters.

---

## 🛠️ Technical Details

### 🔄 Data Preprocessing (`movie.ipynb`)

* **Merging**: Combines movies and credits datasets.

* **Features Used**:

  * `movie_id`, `title`, `overview`, `genres`, `keywords`, `cast`, `crew`

* **JSON Parsing**: Converts stringified JSON fields into lists.

* **Feature Engineering**:

  * Top 3 actors from cast
  * Only director from crew
  * Spaces removed from names
  * Combined into a `tags` field

* **Vectorization**:

  * `CountVectorizer` to create feature vectors
  * Cosine similarity matrix for recommendations

### 🌍 Streamlit App (`movie.py`)

* **Frontend**: Built with Streamlit; styled with Tailwind CSS (via CDN)
* **API Integration**: Fetches posters from TMDB
* **Backend Logic**:

  * Loads `.pkl` files
  * Finds top 5 similar movies
  * Displays titles and posters in a responsive grid

---

## ⚠️ Limitations

* Dataset is static and may not include new releases.
* Does not incorporate user preferences or ratings.
* Requires internet connection for TMDB API.
* Minor Pandas warnings (`SettingWithCopyWarning`) may appear — can be fixed using `.loc`.

---

## 🌱 Future Improvements

* ✅ Add collaborative filtering for user-personalized results.
* 🔄 Update dataset to include newer movies.
* ⚙️ Optimize preprocessing to remove warnings.
* 🎛️ Add filters (e.g., by genre, release year).
* ☁️ Deploy to cloud (Streamlit Sharing, Render, or Hugging Face Spaces).

---

## 🤝 Contributing

Contributions are welcome!
Feel free to submit issues or pull requests for bugs, improvements, or features.

---

## 📜 License

This project is licensed under the **MIT License**.
See the [LICENSE](LICENSE) file for more details.

---

## 🙏 Acknowledgments

* **[TMDB](https://www.themoviedb.org/)** – Movie data and API.
* **[Kaggle](https://www.kaggle.com/)** – Hosting the dataset.
* **[Streamlit](https://streamlit.io/)** – Building the interactive dashboard.

---

Let me know if you'd like a downloadable `.md` file or want this customized further for deployment platforms like Heroku, Hugging Face, or GitHub Pages.
