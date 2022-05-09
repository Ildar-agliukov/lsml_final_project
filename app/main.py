from celery import Celery
from celery.result import AsyncResult
from flask import (
    Flask,
    make_response,
    render_template,
    request,
    jsonify
)

from PIL import Image
import io
from base64 import encodebytes

celery_app = Celery('tasks', backend='redis://redis', broker='redis://redis')
app = Flask(__name__)

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        file = request.files['file']
        file_name = file.filename
        file.save(f'/images/{file_name}')
        task = celery_app.send_task('tasks.predict', [file_name])
    
    return jsonify({"task_id": task.id})



@app.route('/task/<task_id>', methods=['GET', 'POST'])
def task(task_id):
    task = AsyncResult(task_id, app=celery_app)
    if task.ready():
        img = Image.open(f'/images/new_{task.result}')
        img.save(f'static/images/{task.result}')
        res = {
            'ready': task.ready(),
            'result': f'../static/images/{task.result}'
        }
    else:
        res = {
            'ready': task.ready()
        }
    return jsonify(res)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
