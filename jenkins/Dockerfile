FROM jenkins/jenkins:lts

# Install necessary plugins
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt

# Configure Jenkins settings
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"

# Create Jenkins user
RUN groupadd -g 1000 jenkins || true \
    && useradd -d "/var/jenkins_home" -u 1000 -g 1000 -m -s /bin/bash jenkins || true

# Expose Jenkins port
EXPOSE 8080

# Default command
CMD ["tini", "--", "/usr/local/bin/jenkins.sh"]
