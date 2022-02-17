pipeline {
    agent { label 'test-server' }

    stages {


        stage('Cleaning repo data') {
            steps {
                sh "rm -rf alarm"
            }
        }
        stage('Cleaning older files') {
            steps {
                sh "if [ $(docker ps -aq) ]; then docker rm -f $(docker ps -aq);fi;"
            }
        }

        stage('Cloning') {
            steps {
                sh "git clone https://github.com/senolerd/alarm.git"
            }
        }

    }
}

