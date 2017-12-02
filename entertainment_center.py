from media import Movie
import fresh_tomatoes


# Creating instances of class Movie and passing neccessary arguments.
iron_man_3 = Movie("Iron Man 3",
                   "When Stark finds his personal world destroyed at his\
                    enemy's hands, he embarks on a harrowing quest to find\
                    those responsible.",
                   "https://upload.wikimedia.org/wikipedia/en/d/d5/Iron_Man_3_theatrical_poster.jpg",  # NOQA
                   "https://www.youtube.com/watch?v=Ke1Y3P9D0Bc")

interstellar = Movie("Interstellar",
                     "With our time on Earth coming to an end, a team of\
                      explorers undertakes the most important mission in\
                      human history: traveling beyond this galaxy to discover\
                      whether mankind has a future among the stars",
                     "https://i.ytimg.com/vi/Df7IEKqimOY/movieposter.jpg",
                     "https://www.youtube.com/watch?v=zSWdZVtXT7E")

snowden = Movie("Snowden",
                "Snowden, the politically-charged, pulse-pounding\
                 thriller starring Joseph Gordon-Levitt and Shailene\
                 Woodley, reveals the incredible untold personal\
                 story of Edward Snowden, the polarizing figure who\
                 exposed shocking illegal surveillance activities by\
                 the NSA and became one of the most wanted men\
                 in the world.",
                "https://cdn.flickeringmyth.com/wp-content/uploads/2016/12/Snowdenposter.png",  # NOQA
                "https://www.youtube.com/watch?v=QlSAiI3xMh4")

facing_the_giants = Movie("Facing the Giants",
                          "In six years of coaching, Grant Taylor has\
                           never led his Shiloh Eagles to a winning\
                           season.After learning that he and his wife\
                           Brooke face infertility, Grant discovers\
                           that a group of fathers are secretly organizing\
                           to have him dismissed as head coach.",
                          "https://images-na.ssl-images-amazon.com/images/I/51KBHnNDhNL._SX326_BO1,204,203,200_.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=4xneiV7Ru6Q")

war_for_the_planet_of_the_apes = Movie("War for the planet of the Apes",
                                       "In War for the Planet of the Apes,\
                                        the third chapter of the critically\
                                        acclaimed blockbuster franchise,\
                                        Caesar and his apes are forced into\
                                        a deadly conflict with an army of\
                                        humans led by a ruthless Colonel",
                                       "https://upload.wikimedia.org/wikipedia/en/d/d7/War_for_the_Planet_of_the_Apes_poster.jpg",  # NOQA
                                       "https://www.youtube.com/watch?v=JDcAlo8i2y8")  # NOQA

troy = Movie("Troy",
             "An adaptation of Homer's great epic, the film follows\
              the assault on Troy\
              by the united Greek forces and chronicles\
              the fates of the men involved.",
             "https://i.jeded.com/i/troy.11710.jpg",
             "https://www.youtube.com/watch?v=znTLzRJimeY")

# Storing all the movie instances in a list.
movies = [iron_man_3, interstellar, snowden, facing_the_giants,
          war_for_the_planet_of_the_apes, troy]

# Passing the movie list to the function for rendering html file.
fresh_tomatoes.open_movies_page(movies)
