from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

EXCEL_FILE = "book_requests.xlsx"

if not os.path.exists(EXCEL_FILE):
    df = pd.DataFrame(columns=["Name", "Course", "Term", "Book Name", "Author Name", "Edition"])
    df.to_excel(EXCEL_FILE, index=False, engine="openpyxl")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        course = request.form["course"]
        term = request.form["term"]
        book_name = request.form["book_name"]
        author_name = request.form["author_name"]
        edition = request.form["edition"]

        df = pd.read_excel(EXCEL_FILE, engine="openpyxl")
        new_data = pd.DataFrame([[name, course, term, book_name, author_name, edition]], columns=df.columns)
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False, engine="openpyxl")

        return jsonify({"status": "success", "message": "Your book request has been recorded successfully!"})

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
