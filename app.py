from flask import Flask, request, redirect, render_template
import json
import os
import random
import string
from urllib.parse import urlparse
from tlds_list import TLDs

app = Flask(__name__)
BASE_DOMAIN = "http://127.0.0.1:5000"
DATA_FILE = "urls.json"


def load_urls():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}


def save_urls(urls):
    with open(DATA_FILE, "w") as f:
        json.dump(urls, f)


def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))


def validate_url(url):
    """Validate and format URL with HTTPS and proper TLD"""
    parsed = urlparse(url)

    # Add scheme if missing
    if not parsed.scheme:
        url = f"https://{url}"
    elif parsed.scheme == "http":
        url = url.replace("http://", "https://", 1)

    # Re-parse after modifications
    parsed = urlparse(url)

    # Extract domain without port
    domain = parsed.netloc.split(":")[0]

    # Check for TLD validity
    if "." not in domain:
        raise ValueError("URL invalid. Please add a TLD (e.g. .com, .ru, .net, etc.)")

    tld = domain.split(".")[-1]
    if len(tld) < 2 or not tld in TLDs:
        raise ValueError(
            "URL invalid. Please add a proper TLD (e.g. .com, .ru, .net, etc.)"
        )

    return url


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.route("/", methods=["GET", "POST"])
def home():
    error = None
    if request.method == "POST":
        original_url = request.form["url"].strip()
        try:
            original_url = validate_url(original_url)

            urls = load_urls()
            short_code = generate_short_code()

            while short_code in urls:
                short_code = generate_short_code()

            urls[short_code] = original_url
            save_urls(urls)

            shortened_url = f"{BASE_DOMAIN}/{short_code}"
            return render_template("index.html", shortened_url=shortened_url)

        except ValueError as e:
            error = str(e)

    return render_template("index.html", error=error)


@app.route("/<short_code>")
def redirect_to_url(short_code):
    urls = load_urls()
    original_url = urls.get(short_code)
    if original_url:
        return redirect(original_url)
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
