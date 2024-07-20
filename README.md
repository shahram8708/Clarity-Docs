# Clarity Docs 🤖

Clarity Docs is a web application that allows you to upload PDF files, analyze them, and generate insights using advanced AI technologies. The application integrates with the Gemini API to provide detailed summaries and insights, and offers features to view, copy, and listen to the generated summaries.

## Features ✨

- **PDF Upload**: Choose and upload PDF files for analysis.
- **Custom Input**: Provide specific questions or additional input for tailored insights.
- **Document Analysis**: Automatically extract and summarize text from uploaded PDFs.
- **Interactive Summary**: View the summary in Markdown format, copy it, or listen to it using text-to-speech.
- **Loading Animation**: A wave loader animation is displayed while the document is being processed.

## Technologies Used 🚀

- **Flask**: A lightweight WSGI web application framework for Python.
- **Requests**: A simple HTTP library for Python to interact with external APIs.
- **Markdown**: A Python library to convert text into Markdown format.
- **PDF.js**: A JavaScript library for rendering PDF documents.
- **Marked.js**: A JavaScript library for parsing Markdown.

## Getting Started 🏃‍♂️

To get started with Clarity Docs, follow these steps:

### Prerequisites 📦

Ensure you have Python 3.7+ installed on your machine.

### Installation 💻

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/shahram8708/clarity-docs.git
   cd clarity-docs
   ```

2. **Create a Virtual Environment**:

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**:

   ```bash
   python app.py
   ```

   The application will start and can be accessed at `http://127.0.0.1:5000`.

## Usage 📖

1. Open your web browser and navigate to `http://127.0.0.1:5000`.
2. Upload a PDF file using the "Choose PDF File" button.
3. Enter any custom input or questions in the provided textarea.
4. Click the "Analyze Document" button to process the PDF.
5. View the summary in the "Document Insights" section, or use the available buttons to copy the summary or listen to it.

## API Integration 🌐

Clarity Docs integrates with the Gemini API to generate document summaries. Ensure you replace the placeholder API key in `app.py` with your actual API key.

## Contributing 🤝

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.

## License 📝

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact 📧

For any questions or feedback, please reach out to [Shah Ram](mailto:shahram8708@gmail.com).

---

Thank you for using Clarity Docs! 🚀
