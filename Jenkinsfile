pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "7411847325/edulearn-service"
        DOCKER_TAG = "1.0"
        DOCKER_CREDENTIALS = 'DOCKER_CREDENTIALS'
    }
    stages {
        stage ('checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/BhagyashreeUpari/edulearn-service.git'
                
            }
            
        }
        stage ('build docker image'){
            steps {
                sh 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG .'
            }
        }
        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: DOCKER_CREDENTIALS, usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                    sh "docker push $DOCKER_IMAGE:$DOCKER_TAG"
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps { 
                script {
                    sh "helm upgrade --install edulearn ./charts/edulearn -n edulearn --create-namespace --set image.repository=$DOCKER_IMAGE --set image.tag=$DOCKER_TAG"
                }
            }
        }
    }

}
