items = {
    "Movie Mad Max": ["action", "sci-fi", "post-apocalyptic"],
    "Movie The Office": ["comedy", "workplace"],
    "Movie Interstellar": ["sci-fi", "drama", "space"],
    "Movie La La Land": ["romance", "musical", "drama"],
    "Movie Inception": ["sci-fi", "thriller", "mind-bending"],
    "Movie The Notebook": ["romance", "drama"],
    "Movie Mad Max: Fury Road": ["action", "sci-fi", "post-apocalyptic"]
}

print("Welcome to the Digital Matchmaker!")
print("Available genres: action, adventure, sci-fi, comedy, romance, thriller, drama, fantasy, mystery, pop, dance, rock, alternative")

user_input = input("Enter your preferred genres (comma-separated): ")
user_preferences = set([genre.strip().lower() for genre in user_input.split(',') if genre.strip()]) # Use a set for efficient matching

recommendations = []

for item, genres in items.items():
    item_genres_set = set(genres)
    # Calculate similarity based on the number of common genres
    common_genres = len(user_preferences.intersection(item_genres_set))
    if common_genres > 0:
        # Store item, its score, and its genres
        recommendations.append((item, common_genres, genres))

# Sort recommendations by similarity score in descending order
recommendations.sort(key=lambda x: x[1], reverse=True)

print("\n--- Your Top Recommendations ---")

if not recommendations:
    print("No recommendations found based on your preferences. Try different genres!")
else:
    # Display Top N recommendations (e.g., top 5, or all if less than 5)
    top_n = min(len(recommendations), 5) # You can change N here
    for i in range(top_n):
        item, score, genres = recommendations[i]
        print(f"- {item} (Matching Genres: {score}, All Genres: {', '.join(genres)})")
