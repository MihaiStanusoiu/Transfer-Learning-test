FROM jonathonf/manjaro
# RUN pacman -Syu --noconfirm && pacman -S --noconfirm yay

ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

#COPY requirements.txt .
#RUN pip install -r requirements.txt

RUN docker run -it --name minio -p 9000:9000 minio/minio server /data

COPY "venv/src/__init__.py" .
CMD ["python", "__init__.py"]