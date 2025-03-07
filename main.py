from flask import Flask, render_template, request, jsonify, send_file
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

EXCEL_FILE = "book_requests.xlsx"

# Create the Excel file if it doesn't exist
if not os.path.exists(EXCEL_FILE):
    df = pd.DataFrame(
        columns=["Name", "Course", "Term", "Book Name", "Author Name", "Edition", "Publisher", "Submit Date"])
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
        publisher = request.form["publisher"]
        submit_date = datetime.today().strftime("%Y-%m-%d")  # Auto-fills today's date

        # Append new data to the Excel file
        df = pd.read_excel(EXCEL_FILE, engine="openpyxl")
        new_data = pd.DataFrame([[name, course, term, book_name, author_name, edition, publisher, submit_date]],
                                columns=df.columns)
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False, engine="openpyxl")

        return jsonify({"status": "success", "message": "Your book request has been recorded successfully!"})

    return render_template("index.html")


@app.route("/download", methods=["GET"])
def download():
    return send_file(EXCEL_FILE, as_attachment=True, download_name="book_requests.xlsx",
                     mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")


if __name__ == "__main__":
    app.run(debug=True)
