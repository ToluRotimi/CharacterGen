pipeline {
    agent any
    stages {
        stage('Run unit tests') {
            steps {
                sh "bash test.sh"
            }
        }

        stage('Build and push images') {
          steps {
                sh "sudo docker-compose build --parallel"
                sh "sudo docker login -u trot22 -p Redbottlecap1!"
                sh "sudo docker-compose push"
            }
        } 

        stage('Deploy') {
            steps {
                sh "scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml swarm-master:/home/jenkins/docker-compose.yaml"
                sh "scp -i ~/.ssh/ansible_id_rsa nginx.conf swarm-master:/home/jenkins/nginx.conf"
                sh "ansible-playbook -i ansible/inventory.yaml ansible/playbook.yaml"
            }
        } 
    }
}