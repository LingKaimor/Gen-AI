from flask import Flask , render_template , request ,redirect , url_for

#Initialize the Flask application.
app = Flask(__name__)

#The Home Page (GET request)---
@app.route( '/',methods=['GET'])
def index() :
 """
    Renders the main page, which contains the user input form.
    """

    #The 'index.html' file will be automatically looked for in the templates folder.
 return render_template('index.html')

#---The Greeting handler(POST request)---
@app.route('/greet', methods=['POST'])
def greet():
    """
    Handles the form submission (POST) and displays the result.
    It retrieves data submitted by the user from the form using the REQUEST object.
    """
    if request.method == 'POST':
        # Get the value from the form field named 'user_name'
        user_name = request.form.get('user_name')

        if user_name:
            # Render 'result.html' and pass the collected 'user_name' data
            return render_template('result.html', name=user_name)

        # If no name was provided, redirect back to the home page
        return redirect(url_for('index'))


#---Run
if __name__ == '__main__':
    #Ensure this is true when running locally
    print("🚀 Starting Flask Server at http://127.0.0.1:5000/")
    app.run(debug=True)
