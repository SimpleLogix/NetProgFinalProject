
class Question:
    
    '''Represents a single question'''
    def __init__(self):
        self.question = ''
        self.a1 = ''
        self.a2 = ''
        self.a3 = ''
        self.a4 = ''
        self.correct = ''
        self.received = ''

    def fill_the_question(self,q,a1, a2, a3, a4, cor):
        self.question = q
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.correct = cor

    def set_answer(self,answ):
        '''Set answer received from the client'''
        self.received = answ

    # BUG 01: Comparison is incorrect
    def check_correct(self):
        '''Return True if the answer is correct'''
        return int(self.correct) == int(self.received)

    def __str__(self):
        '''String method for the object'''
        return 'Question(question=' + str(self.question) + '\n' +\
                        'Choice a=' + str(self.a1) + '\n' +\
                        'Choice b=' + str(self.a2) + '\n' +\
                        'Choice c=' + str(self.a3) + '\n' +\
                        'Choice d=' + str(self.a4) + '\n' +\
                        'Correct=' + str(self.correct) + '\n' +\
                        'Received=' + str(self.received) + '\n'

if __name__ == '__main__':
    '''Test the module'''
    q = Question()
    q.question = 'Who ate the cake?'
    q.a1 = 'Bear'
    q.a2 = 'Bee'
    q.a3 = 'No one'
    q.a4 = 'What cake?'
    q.correct = '1'
    q.received = '2'
    print(str(q))
