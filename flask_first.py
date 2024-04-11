from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def main():
    if request.method == 'POST':
        number1 = request.form.get('number1', type=float)
        number2 = request.form.get('number2', type=float)
        operation = request.form.get('operation')

        if operation == 'add':
            result = number1 + number2
        elif operation == 'subtract':
            result = number1 - number2
        elif operation == 'multiply':
            result = number1 * number2
        elif operation == 'divide':
            if number2 != 0:
                result = number1 / number2
            else:
                result = 'Invalid Error'
        return render_template('first_template.html', result = result)
    else:
        return render_template('first_template.html', result = None)

if __name__ == '__main__':
    app.run(debug=True)
