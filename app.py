from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')

# Lista para armazenar exemplos de treinamento
training_examples = []

def generate_response(prompt):
    # Adicione seu código aqui para interpretar a solicitação e gerar uma resposta relevante

    # Verifique se o prompt menciona a estrutura e função do DNA de maneira compreensível
    if 'structure and function of DNA that a dumb person can understand' in prompt.lower():
        # Resposta simplificada sobre a estrutura e função do DNA
        response = """
        DNA (Deoxyribonucleic Acid) is like the instruction manual for building and operating living organisms. It's a double-stranded molecule that looks like a twisted ladder.

        Structure:
        - Imagine it as a spiral staircase with steps made of four building blocks (adenine, thymine, cytosine, and guanine).
        - These building blocks pair up (A with T, C with G) to create the rungs of the ladder.

        Function:
        - DNA stores information that guides the development, functioning, and reproduction of all living things.
        - When cells divide, DNA makes copies of itself to pass on the instructions to new cells.
        - It's like a biological recipe book, ensuring that each living thing is made just right.

        For a visual aid, check this [simple DNA diagram](https://example.com/simple_dna_diagram).
        """

    elif 'DNA Sequence' in prompt or 'gene sequence' in prompt:
        # Resposta sobre sequência de DNA e consequências gênicas
        response = """
        A DNA sequence is like the unique code for building and maintaining an organism. It's the order of the building blocks (adenine, thymine, cytosine, and guanine) in the DNA.

        Consequences of a Gene Sequence:
        - Changes in the sequence (mutations) can lead to variations or genetic disorders.
        - Specific sequences guide the production of proteins, influencing traits and functions.
        - Your unique DNA sequence determines your individual characteristics.

        """

    else:
        # Exemplo básico: usar o modelo de geração de texto
        generated_text = generator(prompt, max_length=50, num_return_sequences=1)[0]['generated_text']
        
        # Remova qualquer URL do texto gerado
        response = ' '.join(word for word in generated_text.split() if 'http' not in word)

    # Adicionar o prompt e a resposta aos exemplos de treinamento
    training_examples.append({'prompt': prompt, 'response': response})

    return response







@app.route('/feedback', methods=['POST'])
def feedback():
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        response = request.form.get('response')
        feedback_type = request.form.get('feedback_type')  # Pode ser 'positive' ou 'negative'

        # Adicione lógica aqui para processar o feedback e atualizar o modelo, se necessário
        # Você pode querer incluir uma verificação para garantir que o feedback seja válido

        # Se desejar, você pode usar o feedback para aprimorar o modelo ou a lógica de resposta

        return jsonify({'status': 'success'})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ia', methods=['GET', 'POST'])
def ia():
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        if prompt:
            response = generate_response(prompt)
            return render_template('ia.html', prompt=prompt, response=response)

    return render_template('ia.html')

if __name__ == '__main__':
    app.run(debug=True)
