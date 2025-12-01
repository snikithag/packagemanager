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
        bat """
        python -m pip install --upgrade pip
        python -m pip install -r requirements.txt || python -m pip install numpy
        """
      }
    }
    stage('Run program') {
      steps {
        bat "python app.py"
      }
    }
    stage('Run tests') {
      steps {
        bat """
        python -m pip install pytest
        pytest -q
        """
      }
    }
    stage('Create artifact') {
      steps {
        bat """
        if not exist artifacts mkdir artifacts
        copy app.py artifacts\\ >nul
        copy requirements.txt artifacts\\ >nul
        powershell Compress-Archive -Path artifacts\\* -DestinationPath artifact.zip -Force
        """
        archiveArtifacts artifacts: 'artifact.zip', fingerprint: true
      }
    }
  }
}

