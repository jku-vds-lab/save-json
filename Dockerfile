FROM python:3.10-buster
LABEL maintainer="klaus.eckelt@jku.at"

WORKDIR /save-json
COPY ./ ./

RUN apt-get update
RUN pip install --no-cache-dir -r /save-json/requirements.txt

CMD ["python", "-m", "uvicorn", "save-json.server:app", "--host", "0.0.0.0", "--port", "80"]

EXPOSE 80