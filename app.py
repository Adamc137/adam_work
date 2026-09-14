from flask import Flask, render_template
import subprocess
from flask import request, jsonify

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/course")
def course():
    return render_template("course.html")

@app.route("/prog")
def prog():
    return render_template("prog.html")

@app.route("/ai")
def ai():
    return render_template("ai.html")

@app.route("/math")
def math():
    return render_template("math.html")

@app.route("/check_code")
def check_code():
    return render_template("check.html")

@app.route("/form_up")
def form_up():
    return render_template("form_up.html")


# @app.route('/check_code', methods=['POST'])
# def check_code():
#     user_code = request.json.get('code')
    
#     # Создаем проверочный скрипт с тестами
#     full_code = f"""
# {user_code}
# assert add(2, 2) == 4
# print("Success")
# """
    
#     try:
#         # Запускаем код в изолированном Docker-контейнере (ограничиваем время и память)
#         result = subprocess.run(
#             ["docker", "run", "--rm", "python:3.10-slim", "python3", "-c", full_code],
#             capture_output=True, text=True, timeout=5
#         )
        
#         if result.returncode == 0:
#             return jsonify({"status": "ok", "message": "Верно!"})
#         else:
#             return jsonify({"status": "error", "message": result.stderr})
            
#     except subprocess.TimeoutExpired:
#         return jsonify({"status": "error", "message": "Превышено время ожидания (зацикливание)"})



if __name__ == "__main__":
    app.run(debug=True)