from flask import Flask, render_template, request

app = Flask(__name__)

def readDetailsOfBio(filepath):
    with open(filepath, 'r') as f:
        lines = [line.strip() for line in f]
    name = lines[0].strip()
    age = int(lines[1])
    major = lines[2].strip()
    location = lines[3].strip()
    return name, age, major, location

def readDetailsNoFormat(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]

name, age, major, location = readDetailsOfBio("static\\info.txt")

@app.route("/")
def homePage():
    about = readDetailsNoFormat("static\\about.txt")
    return render_template('base.html', name = name, location = location, aboutMe = about)

@app.route("/form", methods=['GET', 'POST'])
def demoForm():
    name = None
    if request.method == 'POST':
        name = request.form['name']
        
    return render_template('form.html', name=name)

@app.route("/otherpage")
def otherPage():
    space = readDetailsNoFormat("static\\justSpace.txt")
    return render_template('otherpage.html', content=space)

## When running this file directly..

if __name__ == "__main__":
    app.run(debug=True)