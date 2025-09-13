from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/smruti')
def smruti():
    today_key = datetime.now().strftime("%m-%d")
    smruti = smruti_memories.get(today_key)
    return render_template('smruti.html', smruti=smruti)


smruti_memories = {

    "09-12": {
        "date": "September 12, 2025",
        "occurrences": [
            "Memory from today -- 1 year ago:"
        ],
        "picture": "__"
    },
    
    "09-13": {
        "date": "September 13, 2025",
        "occurrences": [
            "Memory from 1 year ago:"
        ],
        "picture": "__"
    },

    "09-14": {
        "date": "September 14, 2025",
        "occurrences": [
            "Memory from today -- 1 year ago:"
        ],
        "picture": "__"
    },

    "09-15": {
        "date": "September 15, 2025",
        "occurrences": [
            "Memory from today -- 1 year ago:"
        ],
        "picture": "__"
    },

    "09-16": {
        "date": "September 16, 2025",
        "occurrences": [
            "Memory from today -- 1 year ago:"
        ],
        "picture": "__"
    },

    "09-17": {
        "date": "September 17, 2025",
        "occurrences": [
            "Memory from today -- 1 year ago"
        ],
        "picture": "__"
    },

}

