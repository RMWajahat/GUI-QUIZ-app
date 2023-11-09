import json    # to deal JSON data
import requests    # making request to APIs
import html             # decoding HTML characters   like &quote;   for   "


# backend functionality

class request_methods:
    
    
    def __init__(self,subject):
        self.questionList = []
        self.score =0 
        self.requestData(subject)
        
        
    
    def requestData(self,Subject):
        with open("urls.json") as f:
            data = json.load(f)
        questions = requests.get(data[Subject])
        questions.raise_for_status()
        questions = questions.json()["results"]
        
        self.questionList = [{"qs":data["question"],"ans":data["correct_answer"]} for data in questions]
    
    
        
    
    def nextQuestion(self):
        if len(self.questionList)==0:
            return
        question = html.unescape(self.questionList[0]["qs"])
        self.questionList = self.questionList[1:]
        
        
        return question
        
    