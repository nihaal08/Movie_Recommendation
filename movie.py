import pickle
import streamlit as st
import requests
from streamlit.components.v1 import html

# Function to fetch movie poster from TMDB API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path', '')
    return f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else "https://via.placeholder.com/500x750?text=No+Poster"

# Function to get movie recommendations
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_names = []
    recommended_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_posters.append(fetch_poster(movie_id))
        recommended_names.append(movies.iloc[i[0]].title)
    return recommended_names, recommended_posters

# Custom HTML for Tailwind CSS and header styling
def render_header():
    html_content = """
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <div class="bg-gradient-to-r from-blue-600 to-indigo-600 text-white p-6 rounded-lg shadow-lg mb-6">
        <h1 class="text-3xl font-bold">🎬 Movie Recommendation Dashboard</h1>
        <p class="mt-2 text-lg">Discover movies similar to your favorites!</p>
    </div>
    """
    html(html_content, height=150)

# Main Streamlit app
def main():
    # Load data
    global movies, similarity
    movies = pickle.load(open('movies_data.pkl', 'rb'))
    similarity = pickle.load(open('similarity_matrix.pkl', 'rb'))

    # Set page config
    st.set_page_config(page_title="Movie Recommendation Dashboard", layout="wide")

    # Render header
    render_header()

    # Sidebar for movie selection
    with st.sidebar:
        st.markdown("### Select a Movie")
        movie_list = movies['title'].values
        selected_movie = st.selectbox("Choose a movie", movie_list, help="Type or select a movie from the list")
        recommend_button = st.button("Get Recommendations", key="recommend_button")

    # Main content
    st.markdown("### Your Movie Recommendations")
    if recommend_button:
        with st.spinner("Fetching recommendations..."):
            recommended_names, recommended_posters = recommend(selected_movie)
        
        # Display recommendations in a grid
        cols = st.columns(5)
        for idx, (name, poster) in enumerate(zip(recommended_names, recommended_posters)):
            with cols[idx]:
                st.markdown(f"""
                <div class="border rounded-lg p-4 shadow-md hover:shadow-lg transition-shadow">
                    <img src="{poster}" class="w-full rounded-md mb-2" alt="{name} poster">
                    <p class="text-center font-semibold">{name}</p>
                </div>
                """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()