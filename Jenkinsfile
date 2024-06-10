pipeline {
    agent any

    stages {
        stage('Clone repository') {
            steps {
                echo 'Cloning repository...'
                git branch: 'CIFAR-10', url: 'https://github.com/grubnev/AML_FinalTask.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Data Quality Tests') {
            agent {
                docker { image 'python:3.8' }
            }
            steps {
                sh '/usr/local/bin/pytest tests/test_data_quality.py'
            }
        }

        stage('Run Model Tests') {
            agent {
                docker { image 'python:3.8' }
            }
            steps {
                sh '/usr/local/bin/pytest tests/test_model.py'
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
                    docker.image('ml_pipeline_project:latest').run('-d -p 8501:8501 --name ml_app')
                }
            }
        }

        stage('Run App Tests') {
            steps {
                sh '/usr/local/bin/pytest tests/test_app.py'
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    sh 'docker stop ml_app && docker rm ml_app'
                }
            }
        }
    }
}
