from utils import login
from utils import sendPageDownPressEvents

from models import Question, Answer, QuestionAnswer


def get_question_topics(browser):
    """
    Returns a list of topics for the question opened in the 
    provided browser instance.
    """
    elem = browser.find_element_by_class_name("question_topics")
    topic_elems = elem.find_elements_by_class_name("topic_name")
    topics = [e.text for e in topic_elems]
    return topics

def get_question(browser):
    """
    Retrieves details about the question opened in the browser instance.
    
    Returns question text and the associated topics.    
    """    
    topics = get_question_topics(browser)
    q_elem = browser.find_element_by_class_name("question_text_edit")
    text_elem = q_elem.find_element_by_tag_name("h1")
    text = text_elem.text

    question = Question(text, topics)
    return question

def get_answers(browser):
    """
    Retrieves the answers for the question opened in the browser.
    
    Returns number of votes, author, question text and author homepage url.    
    """
    sendPageDownPressEvents(browser, 10)
    answer_elems = browser.find_elements_by_class_name("answer_text_wrapper")
    answers = []
    for elem in answer_elems:
        votes = elem.find_element_by_class_name("numbers")
        author_elem = elem.find_element_by_class_name("user")
        text_elem = elem.find_element_by_class_name("answer_content")
        author = unicode(author_elem.text)
        author_url = author_elem.get_attribute("href")
        text = unicode(text_elem.text)
        votes = votes.text
        answer = Answer(votes, author, author_url, text)
        answers.append(answer)
    return answers

def prepareQuesAnsObject(url="https://www.quora.com/2013-year/What-was-the-best-part-of-2013-in-your-opinion"):
    """
    Returns QuestionAnswer instance consisting of the Question and a list of Answer objects
    associated with the question.
    """    
    browser = login()
    browser.get(url)
    
    question = get_question(browser)
    answers = get_answers(browser)
    quesAns = QuestionAnswer(question, answers)
    browser.quit()
    return quesAns   

#QA = prepareQuesAnsObject("https://www.quora.com/Whats-a-good-Mac-app-that-displays-the-lyrics-of-your-iTunes-songs")

#print QA.question.text
#print len(QA.answers)

#browser.quit()


