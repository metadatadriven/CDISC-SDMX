FROM gitpod/workspace-full

RUN sudo apt-get update && \
    sudo apt-get -y install graphviz && \
    wget https://github.com/PowerShell/PowerShell/releases/download/v7.1.0/powershell_7.1.0-1.ubuntu.20.04_amd64.deb && \
    sudo add-apt-repository universe && \
    sudo dpkg --force-all -i powershell_7.1.0-1.ubuntu.20.04_amd64.deb && \
    rm powershell_7.1.0-1.ubuntu.20.04_amd64.deb

