pipeline {
    agent { label 'test-server' }

    stages {
        stage('Hello') {
            steps {
		
                sh "rm -rf alarm"
                sh "git clone https://github.com/senolerd/alarm.git"
		sh "echo test > test.txt"
            }
        }
    }
}
