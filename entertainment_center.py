import fresh_tomatoes
import media

Inception = media.Movie("Inception","2010","Sci-fi/Thriller","2h28m","https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg","https://www.youtube.com/watch?v=66TuSJo4dZM")
Predestination = media.Movie("predestination","2014","Fantasy/Thriller","1h37m","http://t3.gstatic.com/images?q=tbn:ANd9GcTp-yv1Vq_eoOYzyQPRghPbWKAmT3kAP-hGgI-9B8exr5R3uhbU","https://www.youtube.com/watch?v=-FcK_UiVV40")
Gattaca = media.Movie("Gattaca","1997","Thriller/Drama","1h48m","https://upload.wikimedia.org/wikipedia/en/b/bb/Gataca_Movie_Poster_B.jpg","https://www.youtube.com/watch?v=BpzVFdDeWyo")
Looper = media.Movie("Looper","2012","Fantasy/Thriller","1h59m","http://t0.gstatic.com/images?q=tbn:ANd9GcSN2OH-geb6K6TMqpahtBU_CmsoToTcB1vTt8S_fzhFRaQdJ9LV","https://www.youtube.com/watch?v=G90QrEKh8l8")
Brazil = media.Movie("Brazil","1985","Fantasy/Thriller","2h22m","https://upload.wikimedia.org/wikipedia/en/e/e9/Brazil_%281985_film%29_poster.jpg","https://www.youtube.com/watch?v=ZKPFC8DA9_8")
Tron = media.Movie("Tron","2010","Sci-fi/Action","2h7m","http://t1.gstatic.com/images?q=tbn:ANd9GcSchLICLsn0n_GlVBYmaIZjwcYDuqvb1fg4nVvr8WAh3FN8EqfY","https://www.youtube.com/watch?v=L9szn1QQfas")

# store movie objects to movies array
movies = [Inception,Predestination,Gattaca,Looper,Brazil,Tron]

# Call movie trailer page method 
fresh_tomatoes.open_movies_page(movies)