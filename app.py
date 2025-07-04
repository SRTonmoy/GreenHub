from flask import Flask, render_template, redirect, url_for, request, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Dummy user data for authentication
USER_DATA = {
    "username": "sahriarrahman701@gmail.com",
    "password": "41230100828"
}

# Login Route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        # Authenticate user
        if username == USER_DATA["username"] and password == USER_DATA["password"]:
            session["user"] = username  # Store the username in the session
            flash("Login successful!", "success")
            return redirect(url_for("index"))
        else:
            flash("Invalid username or password.", "error")
    
    return render_template("login.html")  # Render login page


# Logout Route
@app.route("/logout")
def logout():
    session.pop("user", None)  # Remove user from session
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))
@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query", "")
    
    # You can process the query here (e.g., search fruits, vegetables, etc.)
    # For example, let's just display the search term on a result page.
    
    # You can replace this with actual data search logic later.
    search_results = {
        "fruits": ["Apple", "Banana", "Mango", "Pineapple"],  # Example data
        "vegetables": ["Carrot", "Broccoli", "Spinach", "Potato"],  # Example data
        "nutrition": ["Vitamin C", "Vitamin A", "Iron", "Calcium"],  # Example data
        "pricing_trends": ["Trend 1", "Trend 2", "Trend 3", "Trend 4"],  # Example data
    }
    
    # Just for demonstration, let's assume all the results are for fruits
    # You can filter the results based on your own logic.
    filtered_results = search_results.get("fruits", [])

    return render_template("search_results.html", query=query, results=filtered_results)


# index Route (Protected)
@app.route("/")
def index():
    if "user" not in session:
        flash("Please log in to access the index.", "warning")
        return redirect(url_for("login"))
    return render_template("index.html")  # Main index page

# Fruits Route
@app.route("/fruits")
def fruits():
    if "user" not in session:
        flash("Please log in to access this page.", "warning")
        return redirect(url_for("login"))
    return render_template("fruits.html")

# Vegetables Route
@app.route("/vegetables")
def vegetables():
    if "user" not in session:
        flash("Please log in to access this page.", "warning")
        return redirect(url_for("login"))
    return render_template("vegetables.html")

# Nutrition Info Route
@app.route("/nutrition")
def nutrition():
    if "user" not in session:
        flash("Please log in to access this page.", "warning")
        return redirect(url_for("login"))
    return render_template("nutrition.html")

# Pricing Trends Route
@app.route("/pricing-trends")
def pricing_trends():
    if "user" not in session:
        flash("Please log in to access this page.", "warning")
        return redirect(url_for("login"))
    return render_template("pricing_trends.html")

if __name__ == "__main__":
    app.run(debug=True)
