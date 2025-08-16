from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to EduLearn LMS Platform! 🚀"

@app.route('/courses')
def courses():
    return {
        "courses": [
            {"id": 1, "name": "DevOps Fundamentals", "duration": "4 weeks"},
            {"id": 2, "name": "AWS Cloud Practitioner", "duration": "3 weeks"},
            {"id": 3, "name": "Python for Beginners", "duration": "5 weeks"}
        ]
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

