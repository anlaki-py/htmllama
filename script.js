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