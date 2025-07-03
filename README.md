Movie Recommendation System
Project Overview
The Movie Recommendation System is a content-based recommendation engine designed to suggest movies to users based on their preferences. It leverages natural language processing (NLP) techniques and cosine similarity to recommend movies similar to a user-selected movie. The system uses the TMDB 5000 Movie Dataset, which includes metadata about movies such as genres, keywords, cast, crew, and overviews. The project consists of two main components:

Data Preprocessing and Model Building (movie.ipynb): A Jupyter Notebook that processes the dataset, creates a recommendation model, and saves the processed data and similarity matrix.
Web Application (movie.py): A Streamlit-based dashboard that allows users to select a movie and view recommendations, complete with movie posters fetched from the TMDB API.

This project is designed to be user-friendly, scalable, and easy to deploy, providing an interactive interface for movie enthusiasts to discover new films.
Features

Content-Based Filtering: Recommends movies based on similarity in genres, keywords, cast, crew, and overview.
Interactive Dashboard: Built with Streamlit, allowing users to select a movie and view up to five recommended movies with posters.
TMDB API Integration: Fetches movie posters dynamically to enhance the user experience.
Efficient Preprocessing: Handles JSON parsing, data cleaning, and feature engineering to create a robust recommendation model.
Scalable Model: Uses cosine similarity for efficient and accurate movie recommendations.

Dataset
The project uses the TMDB 5000 Movie Dataset sourced from Kaggle. The dataset contains metadata for approximately 5,000 movies, including:

Movie titles, IDs, and overviews
Genres and keywords
Cast and crew details

Source: TMDB 5000 Movie Dataset
Project Structure

movie.ipynb: Jupyter Notebook for data preprocessing, model building, and saving artifacts.
movie.py: Streamlit application for the interactive movie recommendation dashboard.
movies_data.pkl: Pickle file containing the processed movie dataset.
similarity_matrix.pkl: Pickle file containing the cosine similarity matrix for recommendations.
README.md: This file, providing an overview and instructions for the project.

Installation
To run this project locally, follow these steps:
Prerequisites

Python 3.8 or higher
Jupyter Notebook (for running movie.ipynb)
Streamlit (for running movie.py)
TMDB API key (for fetching movie posters)

Setup

Clone the Repository:
git clone <repository-url>
cd movie-recommendation-system


Install Dependencies:Create a virtual environment and install the required packages:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

requirements.txt:
numpy
pandas
scikit-learn
streamlit
requests


Obtain TMDB API Key:

Sign up at TMDB and generate an API key.
Ensure the API key is correctly set in movie.py (line: url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=<your-api-key>&language=en-US").


Download the Dataset:

Download the TMDB 5000 Movie Dataset from Kaggle.
Place the tmdb_5000_movies.csv and tmdb_5000_credits.csv files in the project directory.



Running the Project

Preprocess Data and Build Model:

Open movie.ipynb in Jupyter Notebook.
Run all cells to preprocess the dataset, generate the recommendation model, and save movies_data.pkl and similarity_matrix.pkl.

jupyter notebook movie.ipynb


Launch the Streamlit App:

Run the Streamlit application to start the dashboard.

streamlit run movie.py


Open the provided URL (usually http://localhost:8501) in a web browser.



Usage

Select a Movie: Use the dropdown menu in the sidebar to choose a movie from the dataset.
Get Recommendations: Click the "Get Recommendations" button to view five recommended movies.
View Results: Recommendations are displayed with movie titles and posters in a grid layout.

Technical Details
Data Preprocessing (movie.ipynb)

Merging Datasets: Combines tmdb_5000_movies.csv and tmdb_5000_credits.csv on the title column.
Feature Selection: Selects relevant columns (movie_id, title, overview, genres, keywords, cast, crew).
Parsing JSON: Converts JSON strings in genres, keywords, cast, and crew into lists using ast.literal_eval.
Feature Engineering:
Limits cast to the top 3 actors.
Extracts only the director from the crew.
Removes spaces from names to improve vectorization.
Splits the overview into words and combines it with genres, keywords, cast, and crew into a tags column.


Model Building: Uses CountVectorizer to convert tags into numerical vectors and computes a cosine similarity matrix for recommendations.

Streamlit Application (movie.py)

Frontend: Built with Streamlit and styled using Tailwind CSS via a CDN.
API Integration: Fetches movie posters from the TMDB API.
Recommendation Logic: Loads the preprocessed dataset and similarity matrix, then retrieves and displays recommendations based on user input.

Limitations

The system relies on the TMDB 5000 Movie Dataset, which may not include the latest movies.
Recommendations are based on content similarity (genres, keywords, cast, crew, overview) and do not account for user ratings or collaborative filtering.
An active internet connection is required to fetch movie posters via the TMDB API.
The SettingWithCopyWarning in movie.ipynb indicates potential issues with Pandas operations on DataFrame slices. While the code functions correctly, these warnings could be addressed by using .loc for explicit indexing.

Future Improvements

Incorporate collaborative filtering to include user ratings and preferences.
Expand the dataset to include more recent movies.
Optimize the preprocessing pipeline to eliminate Pandas warnings.
Add advanced filtering options (e.g., by genre or year) in the Streamlit app.
Deploy the application to a cloud platform for public access.

Contributing
Contributions are welcome! Please submit a pull request or open an issue on the repository for bug reports, feature requests, or improvements.
License
This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments

TMDB: For providing the movie dataset and API for poster images.
Kaggle: For hosting the TMDB 5000 Movie Dataset.
Streamlit: For the framework used to build the interactive dashboard.
