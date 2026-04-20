from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        foydalanuvchi_nomi = request.form.get('foydalanuvchi_nomi')
        telefon = request.form.get('telefon')
        yosh =  request.form.get('yosh')

        yosh = int(yosh)

        if len(foydalanuvchi_nomi) > 4 and '+' in telefon and len(telefon) >= 11 and yosh >= 18 and yosh <= 99:
            res = [foydalanuvchi_nomi, telefon, yosh]
        else:
            res = ["Ma'lumotlar noto'g'ri kiritildi"]

        return render_template('result2.html', res=res) 

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
