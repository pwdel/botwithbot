FROM python:3.8-slim-buster

# Install TensorFlow and system dependencies
RUN apt-get update && apt-get install -y \
        build-essential \
        libhdf5-dev \
        libc-ares-dev \
        libeigen3-dev \
        libatlas-base-dev \
        libopenblas-dev \
        libblas-dev \
        liblapack-dev \
        gfortran \
        python3-dev \
        python3-pip \
        wget \
        unzip

RUN pip3 install tensorflow==2.2

# Install packages from requirements.txt
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy code from development container
COPY . .

# Set the entry point
CMD ["python", "entrypoint.py"]