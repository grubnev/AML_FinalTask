pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/grubnev/AML_FinalTask.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python -m unittest discover -s src/tests'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('ml_pipeline_project:latest')
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    docker.image('ml_pipeline_project:latest').run('-p 8501:8501')
                }
            }
        }
    }
}
