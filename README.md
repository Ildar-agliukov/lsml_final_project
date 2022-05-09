# LSML2 Final Project 08.05.2022
## The Starry Night Generative Network

### 1. Design document 

Project documentation:  
In my simple project you can generate image like Vincent van Gogh - The Starry Night picture style  
Other style also can be applyed but need more time to implementation.

Schema of work:  
We upload image from frontend to the backend by javascript and Flask   
Next Flask create task to modify image by model and return task_id from celary to the client   
Javascript waiting True ready status and parse new image from backend response   

Reproduce instruction: to train you can simply run jupyter notebook where model will loged by MLFLOW   


The main project idea is a trying to copy some style of picture to image. 
The project was inspired by that paper: https://arxiv.org/pdf/1703.06953.pdf.  
Loss is summ of style network loss and content network losses.  
Content network loss content_weight * MSE between customized Vgg  features outputs original image and style image.  
Style loss is sum of style_weights * MSE betweeb gramm matrix output.  


### 2. Dataset
Dataset is COCO joined train and val dataset that you can download from 

http://images.cocodataset.org/zips/train2014.zip  
http://images.cocodataset.org/zips/val2014.zip  


### 3. Model trained code
I prepare jupyter notebook with mlflow loging final step  
I separate the Mlflow step because I train notebook in Google Colab and it a litle tricke think.
For me it seems like mlflow project



### 4. Docker part 
We have docker compose for full architecture
1) Backend
2) Celery
3) Redis
4) Jupyterlab
6) Mlflow with Database


### Installing:
Simply run docker-compose up --build


To see app go to the - `http://localhost:8080/`.  
Mlflow interface here - `http://localhost:5030/`    
Jupyter - `http://localhost:8060`  
