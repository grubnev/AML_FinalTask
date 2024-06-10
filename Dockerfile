pipeline {
    agent any
    stages {
        stage('Clone repository') {
            steps {
                git 'https://github.com/grubnev/AML_FinalTask.git'
            }
        }
        stage('Setup environment') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                sh 'pytest tests'
            }
        }
        stage('Start Streamlit app') {
            steps {
                sh 'streamlit run app.py'
            }
        }
    }
}