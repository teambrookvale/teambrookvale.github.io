pipeline {
    agent any

    stages {
        stage('Build & Deploy') {
            steps {
                bat '"C:\\Program Files\\Git\\usr\\bin\\ssh.exe" -i C:\\Windows\\System32\\config\\systemprofile\\.ssh\\ec2-key-pair.pem ubuntu@52.64.103.229 "/home/ubuntu/teambrookvale.github.io/pull-and-deploy-jekyll-teambrookvale.sh"'
            }
        }
    }
}
