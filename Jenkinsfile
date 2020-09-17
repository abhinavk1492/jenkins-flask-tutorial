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
                cat <<EOF > set_memory.yaml
                apiVersion: apps/v1
                kind: Deployment
                metadata:
                  name: my-nginx
                spec:
                  template:
                    spec:
                      containers:
                      - name: my-nginx
                        resources:
                        limits:
                          memory: 512Mi
                EOF
             '''
          sh 'kubectl create -f set_memory.yaml'
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
