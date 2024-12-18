pipeline {
    agent any

    environment {
        PYTHON_ENV = "/usr/bin/python3" // Adjust to your Python path
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Pull the latest code from GitHub
                git branch: 'main', url: 'https://github.com/phamgiakiet273/testJenkins.git'
            }
        }
          
        stage('Run Flask Application') {
            steps {
                // Run Flask app in the background
                sh 'nohup ${PYTHON_ENV} /home/ubuntu/jenkins_exercise/app.py &'
            }
        }

        stage('Run Tests') {
            steps {
                // Run test cases
                sh 'pytest /home/ubuntu/jenkins_exercise/tests/test_app.py --maxfail=5 --disable-warnings'
            }
        }
    }

    post {
        success {

        }
        failure {

        }
    }
}
