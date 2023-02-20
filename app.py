from flask import Flask, render_template, jsonify
app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title': 'Data Analyst',
    'location': 'Bengaloo',
    'salary': 'Rs. 1,00,000'
  },
  {
    'id':2,
    'title': 'Front-End',
    'location': 'Delhi',
    'salary': 'Rs. 1,50,000'
  },
  {
    'id':3,
    'title': 'Back-end',
    'location': 'SF',
  },
]

@app.route("/")
def hello():
    return render_template('home.html', 
                           jobs=JOBS, 
                           company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)