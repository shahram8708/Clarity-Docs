from flask import Flask, render_template, request, jsonify
import requests
import logging
import markdown

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

API_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyBc9a2I57vkHjVYhJ42QkzMxZvwq0BY44k"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    text = data.get('text', '')
    custom_input = data.get('customInput', '')
    
    try:
        gemini_response = generate_story(text, custom_input)
        logging.debug(f"API response: {gemini_response}")
        if gemini_response and 'candidates' in gemini_response:
            story_content = extract_story_content(gemini_response)
            if story_content:
                markdown_content = markdown.markdown(story_content)
                return jsonify({'summary': markdown_content})
        return jsonify({'error': 'Failed to generate response. Please try again.'}), 500
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return jsonify({'error': str(e)}), 500

def generate_story(text, custom_input):
    prompt = f"{custom_input} {text}"
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    response = requests.post(API_ENDPOINT, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def extract_story_content(response):
    candidates = response.get('candidates', [])
    if candidates:
        content = candidates[0].get('content', {})
        if content:
            parts = content.get('parts', [])
            if parts:
                return parts[0].get('text', '')
    return None

if __name__ == '__main__':
    app.run(debug=True)
