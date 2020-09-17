pipeline {
  environment {
    registry = "akapula/my-flask-app"
    registryCredential = 'dockerhub_id'
    DOCKER_IMAGE_NAME = "akapula/my-flask-app"
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
      steps {
        withKubeConfig([credentialsId: 'gkesecret', serverUrl: 'https://104.196.96.190', namespace: 'cloudbees-core']) {
          sh '''
                cat <<EOF >./password.txt
                username=admin
                password=secret
             '''
          //sh 'kubectl delete po my-flask'
          //sh 'kubectl create deploy my-flask-deploy --image=$DOCKER_IMAGE_NAME:$BUILD_NUMBER --replicas=3'
          sh 'cat password.txt'
        }
        //input 'Deploy to Production?'
        //milestone(1)
        //implement Kubernetes deployment here
        //kubernetesDeploy(
        //kubeconfigId: 'gkeconfig', configs: 'my-flask-app-kube.yml', enableConfigSubstitution: true)
      }
    }

  }
}
