from flask import Flask, request, render_template

# ==================================================
# インスタンス生成
# ==================================================
app = Flask(__name__)

# ==================================================
# ルーティング
# ==================================================
# GETでデータ取得
@app.route('/get')
def do_get():
    name = request.args.get('name')
    return f'ハロー、 {name}さん！'

# POSTでデータ取得
@app.route('/', methods=['GET', 'POST'])
def do_get_post():
    if request.method == 'POST':
        text = request.form.get('text')
        # cmd = f"python ./jano.py {name}"
        # subprocess.call(cmd.split())
        # wakati = jano.wakati
        import jano
        wakati = jano.keisotai_kaiseki(text)
        return render_template('result.html', text=wakati)
    return render_template('index.html')

# ==================================================
# 実行
# ==================================================
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5001", threaded=True, debug=True)
