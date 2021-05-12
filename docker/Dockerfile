FROM python:3.9
MAINTAINER Resha Dwika Hefni Al-Fahsi (reshalfahsi)

RUN apt-get update \
    && pip install --upgrade pip \
    && pip install \
        --no-cache-dir \
        numpy Pillow opencv-python ggb \
    && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["/bin/bash"]
