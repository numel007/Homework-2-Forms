from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""

    return render_template("froyo_form.html")


@app.route('/froyo_results')
def show_froyo_results():
    """Shows the user what they ordered from the previous page."""
    context = {
    "users_froyo_flavor" : request.args.get('flavor'),
    "users_toppings" : request.args.get('toppings')
    }
    return render_template("froyo_results.html", **context)

@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorites_results" method="GET">
    Favorite color?<br/>
    <input type="text" name="color" placeholder="Favorite color"><br/>
    Favorite animal?<br/>
    <input type="text" name="animal" placeholder="Favorite animal"><br/>
    Favorite city?<br/>
    <input type="text" name="city" placeholder="Favorite city"><br/>
    <input type="submit" value="Submit answers">
    """

@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    fav_color = request.args.get('color') 
    fav_animal = request.args.get('animal') 
    fav_city = request.args.get('city') 
    return f'Wow, I didn\'t know {fav_color} {fav_animal}s lived in {fav_city}!'

@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/message_results" method="POST">
    Enter a secret message<br/>
    <input type="text" name="message">
    <input type="submit" value="Submit message">
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    secret_message = request.form.get('message')
    return f""" Here's your secret message!
    {sort_letters(secret_message)}
    """

@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template("calculator_form.html")

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""

    user_operand1 = request.args.get("operand1")
    user_operand2 = request.args.get("operand2")
    user_operation = request.args.get("operation")
    
    if user_operation == "add":
        result = int(user_operand1) + int(user_operand2)
        selected_operation = "add"
    elif user_operation == "subtract":
        result = int(user_operand1) - int(user_operand2)
        selected_operation = "subtract"
    elif user_operation == "multiply":
        result = int(user_operand1) * int(user_operand2)
        selected_operation = "multiply"
    elif user_operation == "divide":
        result = int(user_operand1) / int(user_operand2)
        selected_operation = "divide"
    else:
        result = "Something went wrong"
        selected_operation = "Something went wrong"
    
    context = {
        "op1" : user_operand1,
        "op2" : user_operand2,
        "result" : result,
        "operation" : selected_operation
    }
    return render_template("calculator_results.html", **context)

# List of compliments to be used in the `compliments_results` route (feel free 
# to add your own!) 
# https://systemagicmotives.com/positive-adjectives.htm
list_of_compliments = [
    'awesome',
    'beatific',
    'blithesome',
    'conscientious',
    'coruscant',
    'erudite',
    'exquisite',
    'fabulous',
    'fantastic',
    'gorgeous',
    'indubitable',
    'ineffable',
    'magnificent',
    'outstanding',
    'propitioius',
    'remarkable',
    'spectacular',
    'splendiferous',
    'stupendous',
    'super',
    'upbeat',
    'wondrous',
    'zoetic'
]

@app.route('/compliments')
def compliments():
    """Shows the user a form to get compliments."""
    return render_template('compliments_form.html')

@app.route('/compliments_results')
def compliments_results():
    """Show the user some compliments."""
    context = {
        # TODO: Enter your context variables here.
    }

    return render_template('compliments_results.html', **context)


if __name__ == '__main__':
    app.run()
