from flask import Flask, request, jsonify
from crawler import crawl_page
from processor import process_data
from ai_analysis import summarize_text

app = Flask(__name__)

@app.route("/")
def home():
    return {"message":"Hello host"}

@app.route("/crawl")
def crawl():

    url = request.args.get("url")

    raw_text = crawl_page(url)

    processed = process_data(raw_text)

    summary = summarize_text(processed, url)

    return jsonify({
        "url": url,
        "summary": summary
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)