# Development Dockerfile
FROM python:3.10-slim as build-base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl git tree htop vim less \
    && apt-get clean && rm -rf /var/lib/apt/lists/*


# Add non-root user to the image
ARG DEBIAN_FRONTEND=noninteractive
ARG USERNAME="developer"
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update && apt-get install -y --no-install-recommends sudo \
    && apt-get clean && rm -rf /var/lib/apt/lists/* \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME \
    && chsh -s /bin/bash $USERNAME

USER $USERNAME

# Install pixi
RUN cd /tmp && curl -fsSL https://pixi.sh/install.sh | sh && \
    echo 'eval "$(pixi completion --shell bash)"' >> ~/.bashrc &&\
    echo 'export PATH="/home/developer/.pixi/bin:$PATH"' >> ~/.bashrc
