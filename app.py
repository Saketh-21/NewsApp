from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form.get("query")
        api_key = "beb5b7e1688b454085704942b905c49a"  # Replace with your News API key

        if not api_key:
            return "Please provide a valid API key."

        url = f"https://newsapi.org/v2/everything?q={query}&from=2023-11-13&sortBy=publishedAt&apiKey={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()  # Check for HTTP errors

            news = response.json()

            if "articles" in news:
                articles = []
                for article_data in news["articles"]:
                    article = {
                        "title": article_data["title"],
                        "description": article_data["description"],
                        "urlToImage": article_data["urlToImage"]
                    }
                    articles.append(article)
                return render_template("index.html", articles=articles)
            else:
                return "No articles found for the given query."

        except requests.exceptions.HTTPError as errh:
            return f"HTTP Error: {errh}"
        except requests.exceptions.ConnectionError as errc:
            return f"Connection Error: {errc}"
        except requests.exceptions.Timeout as errt:
            return f"Timeout Error: {errt}"
        except requests.exceptions.RequestException as err:
            return f"Request Exception: {err}"

    return render_template("index.html", articles=[])

if __name__ == "__main__":
    app.run(debug=True)
