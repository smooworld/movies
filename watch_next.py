# import spacy
import spacy

# Load the spacy model needed
nlp = spacy.load('en_core_web_md')


def next_movie(description):
    # open and load file contents
    movies = open("movies.txt", "r")
    # declare a list to store movie list splint into movie title and description
    split_list = []

    # split movies into title and description and store in list
    for movie in movies:
        split_list.append(movie.split(':'))

    # get number of movies in text file
    count = len(split_list)
    # print(count)
    # declare list to store similarity values
    similarity_list = []

    model_sentence = nlp(description)

    # iterate as many times as the number of movies in the text file
    for i in range(0, count):
        # check similarity between the movie description with the recently watched movie description
        similarity_list.append(nlp(split_list[i][1]).similarity(model_sentence))

    # get the maximum similarity value
    max_similarity = max(similarity_list)
    # get the index of highest similarity value
    max_similarity_index = similarity_list.index(max_similarity)

    # return the movie title similar to recently watched movie
    return split_list[max_similarity_index][0]

# movie description to compare with
hulk_description = """Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""


# call function that gets the next movie description that is similar to the recently watched movie
print("Next Movie Recommended to Watch is: " + next_movie(hulk_description))