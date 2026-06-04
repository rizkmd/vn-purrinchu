# This script contains the questions used in this trivia game. 


# Defining questions:


init python:

    """
    A class for questions. 
    """
    class Question(object):

        """
        A constructor for a Question object. 
        @param question         a string containing the question
        @param a1               a string containing the first answer choice
        @param a2               a string containing the second answer choice
        @param a3               a string containing the third answer choice
        @param a4               a string containing the fourth answer choice
        @param correct          a string containing the same text for the correct answer choice
        @param point_value      an integer representing the question's point value (default is 1)
        """
        def __init__(self, question, a1, a2, a3, a4, correct, point_value = 1):
            self.question = question
            self.a1 = a1
            self.a2 = a2
            self.a3 = a3
            self.a4 = a4
            self.correct = correct
            self.point_value = point_value



# Instantiating Question objects:


# Don't forget to append these questions to question_list in question_list.rpy!


define q1 = Question(question = "Apa bulan kelahiran Purrin?",
                        a1 = "September",
                        a2 = "Agustus",
                        a3 = "Juli",
                        a4 = "Juni",
                        correct = "Juli")


define q2 = Question(question = "Apa makanan kesukaan Purrin?",
                        a1 = "100% halal",
                        a2 = "Mi Instan",
                        a3 = "Seblak",
                        a4 = "Pak Gembus",
                        correct = "100% halal")   


define q3 = Question(question = "Apa minuman kesukaan Purrin?",
                        a1 = "Es teh manis jumbo",
                        a2 = "Josu",
                        a3 = "Air mineral dingin",
                        a4 = "Jus alucard",
                        correct = "Air mineral dingin")   


define q4 = Question(question = "Apa hewan kesukaan Purrin?",
                        a1 = "Ikan sapu-sapu",
                        a2 = "Sucipto",
                        a3 = "Blobfish",
                        a4 = "Ikan biru di Spongebob",
                        correct = "Blobfish")   


define q5 = Question(question = "Apa warna kesukaan Purrin?",
                        a1 = "Hijau",
                        a2 = "Silver",
                        a3 = "Merah",
                        a4 = "Kuning",
                        correct = "Silver")   


define q6 = Question(question = "Apa anime kesukaan Purrin?",
                        a1 = "Haikyuu",
                        a2 = "Jujutsu Kaisen",
                        a3 = "Spy x Family",
                        a4 = "Attack on Titan",
                        correct = "Attack on Titan")  


define q7 = Question(question = "Berikut ini merupakan nama hewan peliharaan Purrin, kecuali...",
                        a1 = "Boris",
                        a2 = "Hilda",
                        a3 = "Miumiu",
                        a4 = "Miku",
                        correct = "Miku")  


define q8 = Question(question = "Apa lagu kesukaan Purrin?",
                        a1 = "Justin Bieber - Catching Feelings",
                        a2 = "Bruno Mars - Grenade",
                        a3 = "Ed Sheeran - Photograph",
                        a4 = "Yuuri - Dried Flower",
                        correct = "Justin Bieber - Catching Feelings")  



# Don't forget to append these question objects to question_list in question_list.rpy!