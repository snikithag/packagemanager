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
        pytest -
