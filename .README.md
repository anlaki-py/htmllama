# [DEMO] htmllama

1. **Ensure Flask is Installed:**
   Make sure Flask is installed in your environment:
   ```sh
   pip install Flask
   ```

2. **Create a Flask Server:**
   Save the following content in a file named `server.py`:
   ```python
   from flask import Flask, request, jsonify, send_from_directory
   from langchain_community.llms import Ollama
   import os

   app = Flask(__name__, static_folder='.', static_url_path='')

   @app.route('/')
   def serve_index():
       return send_from_directory('.', 'index.html')

   @app.route('/invoke', methods=['POST'])
   def invoke():
       data = request.json
       model_name = data.get('model')
       user_input = data.get('input')

       try:
           llm = Ollama(model=model_name)
           result = llm.invoke(user_input)
           return jsonify({'result': result}), 200
       except Exception as e:
           return jsonify({'error': str(e)}), 500

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000, debug=True)
   ```

3. **Create the HTML Interface:**
   Save the following content in a file named `index.html` in the same directory as `server.py`:
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Ollama</title>
       <style>
           body {
               font-family: Arial, sans-serif;
               margin: 0;
               padding: 0;
           }
           #container {
               padding: 20px;
               max-width: 800px;
               margin: auto;
           }
           .section {
               margin-bottom: 20px;
           }
           textarea {
               width: 100%;
               height: 150px;
           }
           select, button {
               display: block;
               margin-top: 10px;
           }
           #output {
               white-space: pre-wrap;
               background-color: #f9f9f9;
               padding: 10px;
               border: 1px solid #ddd;
           }
       </style>
   </head>
   <body>
       <div id="container">
           <h1>Ollama</h1>
           <div class="section">
               <strong>Language Model Selection and Input Handler</strong>
               <select id="modelSelect">
                   <option value="tinyllama">tinyllama</option>
                   <option value="phi3">phi3</option>
                   <option value="codegemma:2b">codegemma:2b</option>
                   <option value="gemma:2b">gemma:2b</option>
                   <option value="qwen:0.5b">qwen:0.5b</option>
                   <option value="deepseek-coder:latest">deepseek-coder:latest</option>
               </select>
               <textarea id="userInput" placeholder="Enter your input here"></textarea>
               <button onclick="submitInput()">Submit</button>
           </div>
           <div class="section" id="outputSection" style="display: none;">
               <strong>Output:</strong>
               <div id="output"></div>
           </div>
           <div class="section">
               <strong>Everything AI says is made up!</strong>
           </div>
       </div>

       <script>
           function submitInput() {
               const model = document.getElementById('modelSelect').value;
               const userInput = document.getElementById('userInput').value;
               
               fetch('/invoke', {
                   method: 'POST',
                   headers: {
                       'Content-Type': 'application/json',
                   },
                   body: JSON.stringify({ model: model, input: userInput }),
               })
               .then(response => response.json())
               .then(data => {
                   document.getElementById('outputSection').style.display = 'block';
                   document.getElementById('output').textContent = data.result;
               })
               .catch((error) => {
                   console.error('Error:', error);
               });
           }
       </script>
   </body>
   </html>
   ```


4. **Run the Flask Server:**
   Open your terminal or command prompt, navigate to the directory where `server.py` and `index.html` are located, and run the Flask server:
   ```sh
   python server.py
   ```
   This will start the Flask server on `http://127.0.0.1:5000`.

5. **Access the Application:**
   Open your web browser and navigate to `http://127.0.0.1:5000`. You should see the interface from the `index.html` file.

6. **Testing the Application:**
   - Select a model from the dropdown menu.
   - Enter some text in the textarea.
   - Click the "Submit" button.

   The JavaScript function `submitInput()` will send the selected model and user input to the Flask backend at the `/invoke` route. The backend will process the input using the selected model and return the result, which will be displayed in the output section.

### Troubleshooting Tips
If you encounter any issues, here are some common troubleshooting steps:

- **Check Console Logs:** Open the developer tools in your browser (usually by pressing `F12` or right-clicking and selecting "Inspect") and check the console for any errors.
  
- **Check Server Logs:** Look at the terminal where you ran the Flask server for any error messages or logs that might indicate what is going wrong.

- **CORS Issues:** If you are running the frontend and backend on different hosts or ports, you might run into Cross-Origin Resource Sharing (CORS) issues. In that case, you can install and configure the `flask-cors` extension:
  ```sh
  pip install flask-cors
  ```
  Then, modify your `server.py` to include:
  ```python
  from flask_cors import CORS

  app = Flask(__name__, static_folder='.', static_url_path='')
  CORS(app)
  ```

This setup should provide a functional static HTML interface that interacts with a Flask backend to process model inputs and return outputs dynamically.
