# TASK 4: MOVIE RECOMMENDATION SYSTEM (With Telugu Movies)

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

# Step 1: Create dataset with Telugu + English movies
data = {
    'title': [
        'Inception', 'Interstellar', 'Titanic', 'Avatar', 'The Dark Knight',
        'Baahubali: The Beginning', 'Baahubali: The Conclusion', 'RRR', 
        'Pushpa: The Rise', 'KGF Chapter 1', 'KGF Chapter 2', 
        'Arjun Reddy', 'Geetha Govindam', 'Jersey', 'Ala Vaikunthapurramuloo'
    ],
    'genre': [
        'Sci-Fi Thriller', 'Sci-Fi Drama', 'Romance Drama', 'Fantasy Adventure', 'Action Crime',
        'Epic Action', 'Epic Action', 'Historical Action', 
        'Action Drama', 'Action Thriller', 'Action Drama', 
        'Romantic Drama', 'Romantic Comedy', 'Sports Drama', 'Family Action Comedy'
    ]
}

# Step 2: Convert to DataFrame
df = pd.DataFrame(data)

# Step 3: Convert text data into vectors
cv = CountVectorizer()
count_matrix = cv.fit_transform(df['genre'])

# Step 4: Compute similarity between movies
similarity = cosine_similarity(count_matrix)

# Step 5: Function to recommend movies
def recommend(movie):
    if movie not in df['title'].values:
        print("❌ Movie not found in database!")
        return
    
    movie_index = df[df['title'] == movie].index[0]
    distances = similarity[movie_index]
    similar_movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    print(f"\n🎬 Recommended movies similar to '{movie}':")
    for i in similar_movies:
        print("➡️", df.iloc[i[0]].title)

# Step 6: User Input
user_movie = input("Enter a movie name: ")
recommend(user_movie)
