pipeline {
    agent { label 'test-server' }

    stages {
        stage('Hello') {
            steps {
		
                sh "rm -rf alarm"
                sh "if [ $(docker ps -aq) ]; then docker rm -f $(docker ps -aq);fi;"
                sh "git clone https://github.com/senolerd/alarm.git"
		        
            }
        }
    }
}

