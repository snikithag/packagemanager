pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Install dependencies') {
      steps {
        bat 'python -m pip install -r requirements.txt'
      }
    }
    stage('Run program') {
      steps {
        bat 'python app.py'
      }
    }
    stage('Run tests') {
      steps {
        bat 'python -m pip install pytest'
        bat 'pytest -q'
      }
    }
    stage('Create artifact') {
      steps {
        bat 'mkdir artifacts'
        bat 'copy app.py artifacts\\'
        bat 'copy requirements.txt artifacts\\'
        bat 'powershell Compress-Archive -Path artifacts\\* -DestinationPath artifact.zip -Force'
        archiveArtifacts artifacts: 'artifact.zip', fingerprint: true
      }
    }
  }
}
