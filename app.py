from flask import Flask, render_template, request

app = Flask(__name__)

def detect_sentiment(text):
    positive_keywords = ["happy", "joy", "excited", "good", "love", "pleasant", "peace", "smile","i love you"]
    negative_keywords = ["angry", "sad", "fear", "alone", "bad", "upset", "stress", "lonely", "depressed","lonely"]
    
    text = text.lower()
    
    positive_count = sum(word in text for word in positive_keywords)
    negative_count = sum(word in text for word in negative_keywords)

    if positive_count > negative_count:
        return "Yov Happy Ga vunnatu vunnav ga kaka masthu jorla vunnav thiiii"
    elif negative_count > positive_count:
        return "em kaadhu le kaka thiy em phikar padaku"
    else:
        return "Edhi Aithe Adhi Ayndhi Chusukundham Thiyyi"

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        result = detect_sentiment(user_input)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
