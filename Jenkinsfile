pipeline {
  environment {
    registry = "akapula/my-flask-app"
    registryCredential = 'dockerhub_id'
    DOCKER_IMAGE_NAME = ''
  }
  agent any
  stages {
    stage('Cloning our Git') {
      steps {
        git([url: 'https://github.com/abhinavk1492/jenkins-flask-tutorial.git', branch: 'master', credentialsId: 'github_id'])
      }
    }
    stage('Building our image') {
      steps {
        script {
          DOCKER_IMAGE_NAME = docker.build registry + ":$BUILD_NUMBER"
        }
      }
    }
    stage('Deploy our image') {
      steps {
        script {
          docker.withRegistry('', registryCredential) {
            DOCKER_IMAGE_NAME.push()
          }
        }
      }
    }
    stage('Clean up Images') {
      steps {
        sh 'docker rmi -f $(sudo docker images -aq) || true'
      }
    }
    stage('DeployToProduction') {
      when {
        branch 'master'
      }
      steps {
        input 'Deploy to Production?'
        milestone(1)
        //implement Kubernetes deployment here
        kubernetesDeploy(
        kubeconfigId: 'kubeconfig', configs: 'train-schedule-kube.yml', enableConfigSubstitution: true)
      }
    }

  }
}
