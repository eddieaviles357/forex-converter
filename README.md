# forex-converter
Live conversion of one currency to another

### Conceptual Exercise 

Answer the following questions below:

- What are the important differences between Python and JavaScript?

		Javascript is a dynamic typed, interpreted, scripting programming language. It's mostly used for creating interactive web pages. Python is also a dynamic-typed, interpreted programming language. The difference between Python and Javascript is that Python uses class inheritance and Javascript uses Prototype inheritance. JS uses curly braces for code blocks and Python uses indentation. Js uses the browser as a console whereas Pythons uses the shell.

  ***

- Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you can try to get a missing key (like "c") _without_ your programming crashing.

```Python
d = {"a": 1, "b": 2}
d.get("c", 3)

d["c"] if "c" in d.keys() else 3
```

***

- What is a unit test?

		Unit test is testing a small piece of code.
  

- What is an integration test?

		An integration test is testing different blocks of codes or modules that are integrated with each other.

___

- What is the role of a web application framework, like Flask?

		Frameworks make it easy for developers to make and start projects faster and less bug-prone. It also comes with documentation and makes unit testing easy.
  
___

- You can pass information to Flask either as a parameter in a route URL (like '/foods/pretzel') or using a URL query param (like 'foods?type=pretzel'). How might you choose which one is a better fit for an application?

		  Url parameters should be used as Subjects of a Page whereas URL query parameters should be used as additional information about a Subject.

___

- How do you collect data from a URL placeholder parameter using Flask?

```Python
from flask import Flask
app = Flask(__name__)
@app.route('/example/<placeholder>')
def example(placeholder):
# we can now use placeholder in this function block

```

___

- How do you collect data from the query string using Flask?

```Python
from flask import Flask, request
app = Flask(__name__)
@app.route('/user')
def user():
	arg = request.args.get("arg")
	# or
	arg = request.args["arg"] # error prone
```
  
___

- How do you collect data from the body of the request using Flask?

  ```Python
from flask import Flask, request
app = Flask(__name__)
@app.route('/page')
def page():
	form_data = request.form.get("first-name")
	# or
	form_data = request.form["first-name"] # error prone
```

- What is a cookie and what kinds of things are they commonly used for?

		Cookies are data stored on the client's browser. Cookies are commonly used for storing relevant data of the user. Examples include products in a shopping cart, user id, or user preferences.

___

- What is the session object in Flask?

		  The session object in Flask is used to track the session data and is signed by the server cryptographically.

___

- What does Flask's `jsonify()` do?

`Flask's jsonify() serializes a Python dict to JSON and returns a Response Object.`
