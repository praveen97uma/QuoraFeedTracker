class Question(object):
    def __init__(self, text="", topics=[]):
        self.text = text
        self.topics = topics

class Answer(object):
    def __init__(self, votes=0, author="", author_url="", text=""):
        self.votes = votes
        self.author = author
        self.author_url = author_url
        self.text = text

class QuestionAnswer(object):
    def __init__(self, question=None, answers=[]):
        self.question = question
        self.answers = answers
