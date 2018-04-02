# imports both the fresh_tomatoes file and the media file
import fresh_tomatoes
import media
# creates objects for multiple instances of the class movie
titanic = media.Movie("Titanic",
                      "http://img.moviepostershop.com/titanic-movie"
                      "-poster-1997-1020339699.jpg",
                      "https://www.youtube.com/watch?v=zCy5WQ9S4c0")

jurassic_park = media.Movie("Jurrasic Park",
                            "http://img.moviepostershop.com"
                            "/jurassic-park-movie-poster-1992-1010141477.jpg",
                            "https://www.youtube.com/watch?v=QWBKEmWWL38")

back_to_the_future = media.Movie("Back To The Future",
                                 "https://www.movieposter.com"
                                 "/posters/archive/main/27/A70-13881",
                                 "https://www.youtube.com/watch?v=qvsgGtivCgs")

pulp_fiction = media.Movie("Pulp Fiction",
                           "http://t2.gstatic.com/images?q=tbn:ANd9GcRz"
                           "_2nKTNlxhVtzbh29kgL3m2ebLv3TlYyzrbyqBtEUxt6mBuZ-",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

the_shawshank_redemption = media.Movie("The Shawshank Redemption",
                                       "http://t0.gstatic.com/images"
                                       "?q=tbn:ANd9GcSkmMH"
                                       "-bEDUS2TmK8amBqgIMgrfzN1"
                                       "_mImChPuMrunA1XjNTSKm",
                                       "https://www.youtube.com/"
                                       "watch?v=6hB3S9bIaco")

the_green_mile = media.Movie("The Green Mile",
                             "http://t3.gstatic.com/images?q=tbn:"
                             "ANd9GcRzAo286udsv_uTTpuBmSc3_"
                             "h-nlUaWHYcUYG6VMAhhPcSDLJF7",
                             "https://www.youtube.com/watch?v=o0jNri5rOY4")

# an array of different movies that
# fresh_tomatoes.py will take in to produce the website
movies = [titanic, jurassic_park, back_to_the_future,
          pulp_fiction, the_shawshank_redemption, the_green_mile]
# a call to fresh_tomatoes.py to open the webpage
fresh_tomatoes.open_movies_page(movies)
