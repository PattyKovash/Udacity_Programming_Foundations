import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life.",
						 "file:///Users/Patchy/Documents/Coding/Udacity_Programming%20Foundations/movies/images/toy_story_movie_poster.jpg",
						 "https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar = media.Movie("Avatar",
					 "A marine on an alien planet.",
					 "file:///Users/Patchy/Documents/Coding/Udacity_Programming%20Foundations/movies/images/avatar_movie_poster.jpg",
					 "https://www.youtube.com/watch?v=d1_JBMrrYw8")


pride_and_prejudice = media.Movie("Pride and Prejudice",
								  "A Jane Austen classic",
								  "file:///Users/Patchy/Documents/Coding/Udacity_Programming%20Foundations/movies/images/pride_and_prejudice_movie_poster.jpg",
								  "https://www.youtube.com/watch?v=7Afx8MGg00g")

movies = [toy_story, avatar, pride_and_prejudice]

fresh_tomatoes.open_movies_page(movies)