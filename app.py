# bar_chart.py
import os
import json
import matplotlib.pyplot as plt

from flask import Flask, request, jsonify

app = Flask(__name__)

img_path ="../imgs"

def bar_chart(numbers, labels, pos, name="chart"):
    plt.bar(pos, numbers, color='orange')
    plt.xticks(ticks=pos, labels=labels)

    if not name.lower().endswith(".png"):
        name += ".png"

    plt.savefig(img_path+name)

    if os.path.exists(img_path+name):
        return 1
    else: return 0


@app.route('/bar', methods=['POST'])
def login():
    data = request.json
    # {stats: {{name: rank}, {etc : etc}}}
    if 'stats' not in data:
        return jsonify({'Error': 'User field is missing'}), 400
    if 'name' not in data:
        return jsonify({'Error: name not in data'}), 400

    stats = data['stats']
    labels = list(stats.keys())
    values = list(stats.values())

    if bar_chart(values, labels, list(range(len(labels))), data['name']):
        return jsonify({'Message': 'Graph successful'}), 200
    return jsonify({'Error': 'Graph unsuccessful'}), 401


if __name__ == '__main__':
    app.run(debug=True, port=5003)
    #add port=##### to change the port the api uses