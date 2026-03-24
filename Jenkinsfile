pipeline {
    agent any

    environment {
        REGISTRY = "localhost:5000"
        IMAGE = "flask-crud-api"
    }

    stages {

        stage('Checkout') {
            steps {
                git url: 'https://github.com/Nirmal1995/Pipline-Project.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r Requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest -q'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $REGISTRY/$IMAGE:latest .'
            }
        }

        stage('Push to Local Registry') {
            steps {
                sh 'docker push $REGISTRY/$IMAGE:latest'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker rm -f flask-api || true
                docker run -d --name flask-api -p 5000:5000 $REGISTRY/$IMAGE:latest
                '''
            }
        }
    }
}