def answer(question):
    question = question.replace("What is ","").replace("?","").replace("plus","+").replace("minus","-").replace("multiplied by","*").replace("divided by","/").split()
    question.insert(0,"(")
    question.insert(4,")")
    q = [x.isalpha() for x in question if x not in ("What","is")]
    if any(q):
        raise ValueError("unknown operation")
    else :
        try:
            return eval(' '.join(question))
        except:
            raise ValueError("syntax error")

