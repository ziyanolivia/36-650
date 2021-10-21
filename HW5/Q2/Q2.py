punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
def punct(mystr):
    no_punct = ""
    for char in mystr:
        if char not in punctuations:
            no_punct = no_punct + char
    return no_punct

mystr = "Hello in 36-650,& other MSP courses."
print(punct(mystr))
