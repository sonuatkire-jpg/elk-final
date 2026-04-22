FROM jenkins/jenkins:lts

# Install necessary plugins
RUN /usr/local/bin/install-plugins.sh \
    git \
    docker \
    workflow-aggregator \
    github \
    github-branch-source \
    pipeline-github-lib \
    pipeline-stage-view \
    docker-workflow

# Configure Jenkins settings
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"

# Create Jenkins user
RUN groupadd -g 1000 jenkins \
    && useradd -d "/var/jenkins_home" -u 1000 -g 1000 -m -s /bin/bash jenkins

# Expose Jenkins port
EXPOSE 8080

# Default command
CMD ["/sbin/tini", "--", "/usr/local/bin/jenkins.sh"]