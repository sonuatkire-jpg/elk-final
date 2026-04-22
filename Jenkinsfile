pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = 'elk-post'
        DOCKER_COMPOSE_FILE = 'docker-compose.yml'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/sonuatkire-jpg/elk-post.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker-compose -f ${DOCKER_COMPOSE_FILE} build'
            }
        }

        stage('Test') {
            steps {
                sh 'docker-compose -f ${DOCKER_COMPOSE_FILE} up -d'
                sh 'sleep 30'
                sh 'docker-compose -f ${DOCKER_COMPOSE_FILE} ps'
            }
        }

        stage('Deploy Pipeline') {
            steps {
                // Copy the pipeline configuration to Logstash
                sh 'docker cp pipelines/bank_pipeline.conf elk_logstash_1:/usr/share/logstash/pipeline/bank_pipeline.conf'
                
                // Restart Logstash to reload the pipeline
                sh 'docker-compose -f ${DOCKER_COMPOSE_FILE} restart logstash'
                
                // Wait for Logstash to restart
                sh 'sleep 30'
            }
        }

        stage('Verify') {
            steps {
                // Check if the pipeline is active in Elasticsearch
                sh 'curl -X GET "http://localhost:9200/_ingest/pipeline/bank_pipeline?pretty"'
                
                // Check Logstash status
                sh 'curl -X GET "http://localhost:9600/_node/stats/pipelines?pretty"'
            }
        }
    }

    post {
        always {
            // Clean up containers
            sh 'docker-compose -f ${DOCKER_COMPOSE_FILE} down'
        }
    }
}