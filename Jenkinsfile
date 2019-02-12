pipeline {
    agent any

    environment { 
    }

    stages {
        stage('Build') {
            steps {
                bat '"C:\\Program Files\\Git\\usr\\bin\\ssh.exe" -i ~/.ssh/ec2-key-pair.pem ubuntu@52.64.103.229 "/home/ubuntu/teambrookvale.github.io/deploy-jekyll-teambrookvale.sh"'
            }
        }
        stage('Test') {}
        stage('Deploy') {}
    }
}
