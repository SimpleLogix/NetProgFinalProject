from Question import *

# Creates a Quiq objec out of Question object
class Quiz():
    '''This class creates a quiz of N questions
       Each playr can have its own pace anwering questions
    '''
    def __init__(self):
        self.Questions = []
        self.NUMBER_OF_QUESTIONS = 10
        # len(self.QUESTIONS) # is set to zero initially

    def init_quiz_questions(self):
        '''Create 10 empty question objects'''
        for i in range(0,self.NUMBER_OF_QUESTIONS):
            self.Questions.append(Question())

    def fill_questions(self,q,a,b,c,d,cr):
        '''Insert fields into each question'''
        for i in range(0,len(self.Questions)):
            self.Questions[i].fill_the_question(q,a,b,c,d,cr)

if __name__ == '__main__':
    '''Test the module'''
    q = Quiz()
    q.init_quiz_questions()
    q.fill_questions('question','a','b','c','d','1')
    # Check 10 questions
    for i in range(0, len(q.Questions)):
        print(str(q.Questions[i]))
