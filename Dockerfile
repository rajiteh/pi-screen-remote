FROM python:3.7-buster
ENV PYTHONIOENCODING=UTF-8
ENV PYTHONUNBUFFERED=1
RUN rm -f $(which lsb_release)
WORKDIR /app
ADD requirements.txt .
RUN pip3 install --user -r requirements.txt
ADD . .
CMD [ "python3", "server.py"]