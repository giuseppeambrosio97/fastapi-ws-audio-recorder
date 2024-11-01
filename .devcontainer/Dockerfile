# Use the official Python 3.11 slim image as a base
FROM python:3.11-slim

# Set a default working directory
WORKDIR /workspace

# Install dependencies for creating a non-root user and setting permissions
RUN apt-get update && apt-get install -y \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create the 'vscode' user with sudo privileges
RUN useradd -m -s /bin/bash vscode \
    && echo "vscode ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/vscode \
    && chmod 0440 /etc/sudoers.d/vscode

# Set ownership of the workspace to the vscode user
RUN chown -R vscode:vscode /workspace


RUN pip install poetry
