FROM ubuntu:22.04
ARG DEBIAN_FRONTEND=noninteractive

# Update default packages
RUN apt-get update && apt-get install -y \
    build-essential \
    curl

RUN curl -y --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Install TensorFlow and system dependencies
RUN apt-get update && apt-get install -y \
        build-essential \
        curl \
        libhdf5-dev \
        libblas-dev \
        libc-ares-dev \
        libcairo2-dev \
        libeigen3-dev \
        libatlas-base-dev \
        libopenblas-dev \
        libpango1.0-dev \
        liblapack-dev \
        libssl-dev \
        gfortran \
        python3-dev \
        python3-pip \
        pip \
        binutils \
        gcc \
        libc-dev \
        libc6 \
        # libgcc-s1 \
        libstd-rust-dev \
        cargo \
        rustc \
        wget \
        unzip


# Upgrade Pip
RUN pip install --upgrade pip

# Install packages from requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy code from development container
COPY ./volumebindmount ./home

# Set the working directory to /home
WORKDIR /home
# Set the entry point
CMD /bin/python3.10 app.py