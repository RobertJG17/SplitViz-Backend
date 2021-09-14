import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from splitgate import Splitgate


app = Flask(__name__)


@app.route("/post_test", methods=["POST"])
def post_test():
    info = request.json

    items = []

    for obj in info:
        platform, pid = obj["platform"], obj["pid"]
        player = Splitgate(platform=platform, pid=pid, api_key=api_key)
        player.fetch_stats()
        player.format_stats()
        items.append({player.pid:player.refined_stats})

    return jsonify(items)


if __name__ == '__main__':
    
    # Pulling API key from env file
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    api_key = os.environ.get('API_KEY')

    app.run()