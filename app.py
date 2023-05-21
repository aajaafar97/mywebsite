from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    project_data = [
        {'name': 'Project 1', 'description': 'Redlining Detroit', 'link': 'https://github.com/aajaafar97/Redlining_Detroit'},
        {'name': 'Project 2', 'description': 'Baseball players, degrees of seperation', 'link': 'https://github.com/aajaafar97/507finalaajaafar'},
        # Add more projects as necessary...
    ]
    return render_template('projects.html', projects=project_data)



if __name__ == '__main__':
    app.run(debug=True)