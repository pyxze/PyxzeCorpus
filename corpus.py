from flask import Flask
from flask import request
app = Flask(__name__)

form = '''
<div style="width: 450px; margin: 0 auto;">
<form name="input" action="/" method="post">
<textarea name="text" cols=55 rows=10>%s</textarea>
<br /><div style="float: right;"><input type="submit" value="Submit"></div>
</form>
</div>
''' 

boiler = '''We draw attention to and explore the media's representations of these varying forms of exceptionalism in order to elucidate how and why youths' shared economic plight are culturally elaborated distinctly. But we also do so in order to highlight the ways in which these elaborations, and the victims, villains, and heroes they chose to portray, have affective and material consequences for young people living within and beyond the parameters of the normative life courses that each culture sets out and strives to reinforce. As social scientists, we look to the possibilities imaginable beyond such strictures, but nonetheless recognize the power that national narratives hold as a way of organizing bewildering conditions and experiences into a legible reality.'''

def corpus(text):
    import random

    split = text.split(" ")

    library = {"START": []}
    state = "start"
    for i in split:
        if state == "start":
            library["START"].append(i)
            state = "middle"
            library[i] = []
        elif i.endswith("."):
            i = i.rstrip(".")
            if i not in library:
                library[i] = []
            library[last].append(i)
            library[i].append("STOP")
            state = "start"
        elif state == "middle":
            if i not in library:
                library[i] = []
            library[last].append(i)
        last = i

    next = random.randrange(library["START"].__len__())
    gen = []
    word = library["START"][next]
    gen.append(word)
    last = word
    while last != "STOP":
        next = random.randrange(library[last].__len__())
        word = library[last][next]
        gen.append(word)
        last = word
    gen.pop()
    potion = '''<div style="width: 450px; margin: 0 auto;">''' + " ".join(gen) + "." + '''</div>'''
    return form % text + potion

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':	
        text = request.form['text']
        return corpus(text)
    else:
        return form % boiler

if __name__ == "__main__":
    app.debug = True
    app.run()
