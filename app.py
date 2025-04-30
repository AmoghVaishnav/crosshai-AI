
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from src.model_engine.code_suggester import CodeSuggester

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

suggester = CodeSuggester(db_path="src/knowledge_base/prompt_db.json")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/suggest', methods=['POST'])
def suggest_code():
    data = request.json
    user_code = data.get("code", "").strip()
    user_prompt = data.get("prompt", "").strip()

    if not user_code or not user_prompt:
        return jsonify({"error": "Missing code or prompt"}), 400

    answer, sample_code, code_analysis = suggester.MatchPrompt(user_prompt, user_code)

    return jsonify({
    "prompt": user_prompt,
    "original_code": user_code,
    "suggested_answer": answer,
    "suggested_code": sample_code,
    "code_analysis": code_analysis
})
if __name__ == '__main__':
    app.run(debug=True)
