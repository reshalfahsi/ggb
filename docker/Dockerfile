FROM python:3.6-slim-jessie
MAINTAINER Resha Dwika Hefni Al-Fahsi (reshalfahsi)

RUN buildDeps='build-essential gcc gfortran python3-dev' \
    && apt-get update \
    && apt-get install -y $buildDeps --no-install-recommends \
    && apt-get install -y libopenblas-dev liblapack-dev libfreetype6-dev libpng-dev pkg-config \
    && /usr/local/bin/pip install \
        --upgrade pip \
    && CFLAGS="-g0 -Wl,--strip-all -I/usr/include:/usr/local/include -L/usr/lib:/usr/local/lib" \
        /usr/local/bin/pip install \
        --no-cache-dir \
        --compile \
        --global-option=build_ext \
        --global-option="-j 4" \
        numpy Pillow opencv-python ggb \
    && apt-get purge -y --auto-remove $buildDeps \
    && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["/bin/sh"]
