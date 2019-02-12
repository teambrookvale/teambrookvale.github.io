pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat '"C:\\Program Files\\Git\\usr\\bin\\ssh.exe" -i C:\\Windows\\System32\\config\\systemprofile\\.ssh\\ec2-key-pair.pem ubuntu@52.64.103.229 "/home/ubuntu/teambrookvale.github.io/deploy-jekyll-teambrookvale.sh"'
            }
        }
        stage('Test') {
            steps {
                bat 'echo "No test steps"'
            }
        }
        stage('Deploy') {
            steps {
                bat 'echo "No deploy steps as deployment should have occurred in the Build stage"'
            }
        }
    }
}
