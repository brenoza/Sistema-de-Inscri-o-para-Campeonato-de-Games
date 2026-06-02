from flask import Flask, flask, render_template , request

app = Flask(__name__)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():

    mensagem = ""

    if request.method == 'POST':
        nome = request.form.get('nome')
        if not nome:
            mensagem = "O campo nome é obrigatorio!"
        else:
            mensagem = f"Inscrição realizada com sucesso, {nome}"
            return render_template('cadastro.html', mensagem=mensagem)
        jogo = request.form.get('jogo')
        if not jogo:
            mensagem = "O campo jogo é obrigatorio!"
        else:
            mensagem = f"Inscrição realizada com sucesso, {jogo}"
            return render_template('cadastro.html', mensagem=mensagem)
        email = request.form.get('email')
        if not email:
            mensagem = "O campo e-mail é obrigatorio!"
        else:
            mensagem = f"Inscrição realizada com sucesso, {email}"
            return render_template('cadastro.html', mensagem=mensagem)

        if __name__ == '__main__':
            app.run(debug=True)

            