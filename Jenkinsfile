pipeline {
    agent { label 'test-server' }

    stages {


        stage('Cleaning repo data') {
            steps {
                sh "rm -rf *"
            }
        }
        stage('Cleaning older files') {
            steps {
                sh '''
                    #!/bin/bash
                    if [ $(docker ps -aq) ]; then docker rm -f $(docker ps -aq);fi;
                '''
            }
        }

        stage('Cloning') {
            steps {
                sh '''git clone https://github.com/senolerd/alarm.git'''
            }
        }

        stage('Building') {
            steps {
                sh '''
                    #!/bin/bash
                    cd alarm-backend
                    docker build -t alarm:latest .
                '''
            }
        }

    }
}

