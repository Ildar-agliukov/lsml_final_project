import numpy as np
from celery import Celery
import torch
from PIL import Image
from torch.autograd import Variable
import numpy as np
import mlflow

celery_app = Celery('tasks', backend='redis://redis', broker='redis://redis')


url = f'http://mlflow:5000'
exp_name = 'gen_new_exp'

mlflow.set_tracking_uri(url)
client = mlflow.tracking.MlflowClient(url)
exp = client.get_experiment_by_name(exp_name)
run_info = client.list_run_infos(exp.experiment_id)[-1]
model_uri = "runs:/{}/model".format(run_info.run_id)
model = mlflow.pytorch.load_model(model_uri)
model.eval()

img = Image.open('styles/starry_night.jpg').convert('RGB')
img = img.resize((512, 512), Image.ANTIALIAS)
img = np.array(img).transpose(2, 0, 1)
img = torch.FloatTensor(img).unsqueeze(0)
batch = img.transpose(0, 1)
(r, g, b) = torch.chunk(batch, 3)
batch = torch.cat((b, g, r))
batch = batch.transpose(0, 1)
style_v = Variable(batch, requires_grad=False)
model.setTarget(batch)

@celery_app.task(name='tasks.predict')
def predict(file_name):
    print(f'/images/{file_name}')
    img = Image.open(f'/images/{file_name}').resize((128, 128))
    img = np.array(img)
    img = torch.FloatTensor(img).permute((2, 1, 0)).unsqueeze(0)
    new_img = np.uint8(model(img)[0].clamp(0, 255).detach().permute((2, 1, 0)).numpy())
    new_img = Image.fromarray(new_img, 'RGB')
    new_img.save(f'/images/new_{file_name}')
    return f'{file_name}'
