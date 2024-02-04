from flask import Flask, render_template, redirect, request, flash

from database import User, add_to_db

app = Flask(__name__)
app.secret_key = 'thisissupersecretkeyfornoone'

# Dummy user for demonstration purposes
dummy_user = User(username='dummy', email='dummy@example.com', password='dummy_password')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print("Email =>", email)
        print("Password =>", password)
        # Logic for login
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        cpassword = request.form.get('cpassword')
        print(username, email, password, cpassword)
        # Logic for registration
        if len(username) == 0 or len(email) == 0 or len(password) == 0 or len(cpassword) == 0:
            flash("All fields are required", 'danger')
            return redirect('/register')  # Reload the page
        user = User(username=username, email=email, password=password)
        add_to_db(user)
    return render_template('register.html')

@app.route('/add/job', methods=['GET', 'POST'])
def add_job():
    if request.method == 'POST':
        job_title = request.form.get('job_title')
        job_description = request.form.get('job_description')
        print("Job Title =>", job_title)
        print("Job Description =>", job_description)
        # Logic for adding a job
    return render_template('add_job.html')

@app.route('/add/resume', methods=['GET', 'POST'])
def add_resume():
    if request.method == 'POST':
        full_name = request.form.get('fullName')
        resume_file = request.files.get('resumeFile')
        print("Full Name =>", full_name)
        print("Resume File =>", resume_file.filename)
        # Logic for adding a resume
    return render_template('add_resume.html')

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    # Dummy user data for demonstration purposes
    user_name = [{'username': dummy_user.username}]
    
    if request.method == 'POST':
        # Handle settings form submission
        if 'new_username' in request.form:
            new_username = request.form.get('new_username')
            print("New Username =>", new_username)
            # Add logic to update the username in the database
            # Flash a success or error message accordingly

        elif 'old_pwd' in request.form and 'new_pwd' in request.form and 'confirmation' in request.form:
            old_password = request.form.get('old_pwd')
            new_password = request.form.get('new_pwd')
            confirmation = request.form.get('confirmation')
            print("Old Password =>", old_password)
            print("New Password =>", new_password)
            print("Confirmation =>", confirmation)
            # Add logic to update the password in the database
            # Flash a success or error message accordingly

    return render_template('settings.html', user_name=user_name)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
