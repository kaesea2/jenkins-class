pipeline {
    agent any

    stages {
        stage('Checkout from github') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/kaesea2/jenkins-class.git']])
            }
        }
        stage('Build and Test') {
            steps {
                sh 'python3 test.py'
            }
        }
        stage('Build and run') {
            steps {
                sh 'python3 mytest.py'
            }
        }
        stage('Completed') {
            steps {
                echo 'completed!!!'
            }
        }
    }
}
