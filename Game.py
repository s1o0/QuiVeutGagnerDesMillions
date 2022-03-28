import random
def getQuestion(num:int):

    with open(f'./Questions/q{num}.txt') as file:
        lines=file.readlines()
        numberLines = len(lines)
        randomI = random.randint(0,numberLines-1)
        question = lines[randomI]
        liste = question.split(';')

        
            
        questionP = liste[0].encode('latin-1').decode('utf-8')
        rep1=liste[1].encode('latin-1').decode('utf-8')
        rep2=liste[2].encode('latin-1').decode('utf-8')
        rep3=liste[3].encode('latin-1').decode('utf-8')
        rep4=liste[4].encode('latin-1').decode('utf-8')
        bonneRep=liste[5]
            

        return questionP,rep1,rep2,rep3,rep4,bonneRep







    