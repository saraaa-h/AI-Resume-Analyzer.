# import stuff we need for flask and pandas
from flask import Flask, render_template, request
import pandas as pd #to read CSV
from ai import ask_ai #ollama
#  the flask app
app = Flask(__name__)


@app.route('/') # main page route
def home():
    
    return render_template('index.html')  #  show the index page

#to process skills and show match jobs
@app.route('/analyze', methods=['POST'])
def analyze():
# get skills from the html form input
    user_skills = request.form.get('skills', '').lower()
    
# get feedback from ai fun
    ai_response = ask_ai(user_skills)
    
# read the jobs csv usin pandas
    df = pd.read_csv('jobs.csv')
    
# empty list to store matching jobs
    matched_jobs = []
    
# split input into a list of skills
    skill_list = [s.strip() for s in user_skills.split(',') if s.strip()]
    
# loop through all jobs in the pandas dataframe
    for index, row in df.iterrows():
        job_skills = row['required_skills'].lower()
        
 # check if any skill matches the job requirements
        for skill in skill_list:
            if skill in job_skills:
# add matchin job to my list n stop checkin this job
                matched_jobs.append(row.to_dict())
                break
                
# send data to results.html usin jinja2
    return render_template('results.html', user_skills=user_skills, ai_response=ai_response, jobs=matched_jobs)

# run the flask app
if __name__ == '__main__':
    app.run(debug=True)