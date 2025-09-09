from flask import Flask, request, jsonify

app = Flask(__name__)

notes = []

@app.route("/")
def home():
    return "📝 Welcome to Notes App APIsss fater making changes by AFNAN.again..enabled POLL SCM now..."

@app.route("/notes", methods=["GET"])
def get_notes():
    return jsonify(notes)

@app.route("/notes", methods=["POST"])
def add_note():
    data = request.get_json()
    note = data.get("note")
    if note:
        notes.append(note)
        return jsonify({"message": "Note added!", "notes": notes}), 201
    return jsonify({"error": "Note content is required"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
