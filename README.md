# Vegetable_Classification_DeepLearning_MLOPS_AWS
## Project Description

### Overview:
The Vegetable Classification project aims to employ deep learning, specifically Convolutional Neural Networks (CNNs), for the classification of various types of vegetables based on images. The project will utilize the VGG16 architecture as the base model, implement data augmentation techniques to enhance model performance, and deploy the model as a web application on Amazon Web Services (AWS) Elastic Compute Cloud (EC2) and Elastic Container Registry (ECR). HTML, CSS, and Flask will be used to create the web interface, while GitHub Actions will be employed for Continuous Integration and Continuous Deployment (CI/CD). Docker containers will be utilized to streamline access and scalability.

### Key Features:

1. Data Collection and Preprocessing:
        Gather a comprehensive dataset of vegetable images, ensuring accurate labeling and data organization.
        Preprocess and augment the dataset, including resizing, normalization, and applying transformations to improve model robustness.

2. Model Development:
        Utilize the VGG16 architecture, a well-established CNN pretrained on ImageNet, as the foundational model.
        Fine-tune the top layers of the VGG16 model to adapt it to the vegetable classification task.
        Train the model using the preprocessed dataset.

3. Web Application Creation:
        Build an intuitive web application using HTML and CSS, allowing users to upload images for classification.
        Implement Flask, a Python web framework, to handle image uploads, perform model inference, and display classification results.
        Deploy the web application on an AWS EC2 instance for public access.

4. Continuous Integration and Deployment:
        Establish CI/CD pipelines using GitHub Actions to automate testing and deployment workflows.
        Ensure that code changes are thoroughly tested and deployed to the AWS server, ensuring a reliable and robust application.

5. Docker Containers:
        Containerize the web application and its dependencies using Docker, simplifying deployment and scalability.
        This enables straightforward deployment and scaling as needed.

### Project Workflow:

1. Data Collection and Preprocessing: Collect and preprocess a diverse dataset of vegetable images, properly labeling and augmenting the data.
2. Model Building: Utilize the VGG16 architecture, adapt it for vegetable classification, and train it using the preprocessed dataset.
3. Web Application Development: Create a user-friendly web application using HTML, CSS, and Flask. Implement features for image uploads, model inference, and results presentation.
4. CI/CD with GitHub Actions: Set up CI/CD pipelines on GitHub to automate testing and deployment of code changes.
5. Docker Containerization: Containerize the web application using Docker for ease of deployment and scalability.
6.  Deployment on AWS: Host the web application on an AWS EC2 instance to make it accessible to users.

### Expected Outcomes:

- A user-friendly web application for uploading and classifying vegetable images.
- Precise and efficient vegetable classification using the VGG16-based deep learning model.
- Automated CI/CD pipeline for streamlined development and deployment.
- Docker containers for easy scaling and access.
- A fully deployed web application on an AWS EC2 instance.


## Development Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml

# How to run?

### STEPS:

Clone the repository

```bash
https://github.com/entbappy/Chicken-Disease-Classification--Project
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n cnncls python=3.8 -y
```

```bash
conda activate cnncls
```

### STEP 02- install the requirements

```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,

```bash
open up you local host and port
```

### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

    #with specific access

    1. EC2 access : It is virtual machine

    2. ECR: Elastic Container registry to save your docker image in aws


    #Description: About the deployment

    1. Build docker image of the source code

    2. Push your docker image to ECR

    3. Launch Your EC2

    4. Pull Your image from ECR in EC2

    5. Lauch your docker image in EC2

    #Policy:

    1. AmazonEC2ContainerRegistryFullAccess

    2. AmazonEC2FullAccess

## 3. Create ECR repo to store/save docker image

    - Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken

## 4. Create EC2 machine (Ubuntu)

## 5. Open EC2 and Install docker in EC2 Machine:

    #optinal

    sudo apt-get update -y

    sudo apt-get upgrade

    #required

    curl -fsSL https://get.docker.com -o get-docker.sh

    sudo sh get-docker.sh

    sudo usermod -aG docker ubuntu

    newgrp docker

# 6. Configure EC2 as self-hosted runner:

    setting>actions>runner>new self hosted runner> choose os> then run command one by one

# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app

# AZURE-CICD-Deployment-with-Github-Actions

## Save pass:

s3cEZKH5yytiVnJ3h+eI3qhhzf9q1vNwEi6+q+WGdd+ACRCZ7JD6

## Run from terminal:

docker build -t chickenapp.azurecr.io/chicken:latest .

docker login chickenapp.azurecr.io

docker push chickenapp.azurecr.io/chicken:latest

## Deployment Steps:

1. Build the Docker image of the Source Code
2. Push the Docker image to Container Registry
3. Launch the Web App Server in Azure
4. Pull the Docker image from the container registry to Web App server and run
