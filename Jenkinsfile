pipeline {
    agent any

    stages {
        stage('Clone repository') {
            steps {
                echo 'Cloning repository...'
                git branch: 'main', url: 'https://github.com/grubnev/AML_FinalTask.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
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
            docker.image('ml_pipeline_project:latest').run('-p 8501:8501 --name ml_app --rm')
        }
    }
}

    }
}
