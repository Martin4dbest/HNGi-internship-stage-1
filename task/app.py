from datetime import datetime
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('/index.html')

@app.route('/api', methods=['GET'])
def api():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    current_day = datetime.now().strftime('%A')
    utc_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    response = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': utc_time,
        'track': track,
        'github_file_url': "https://github.com/Martin4dbest/HNGi-internship-stage-1/blob/main/task/app.py",
        'github_repo_url': "https://github.com/Martin4dbest/HNGi-internship-stage-1",
        'status_code': 200
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True)
