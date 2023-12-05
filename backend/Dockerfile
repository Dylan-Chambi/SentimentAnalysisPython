FROM python:3.11
ENV PORT 8080

COPY requirements.txt /
COPY special_requirements.txt /
RUN pip install -r requirements.txt
RUN pip install -r special_requirements.txt -f https://download.pytorch.org/whl/torch_stable.html

RUN python -m spacy download es_core_news_md


COPY ./src /src

COPY app.py /app.py

RUN rm -rf src/models/multilingual-sentiment && rm -rf src/models

RUN mkdir src/models && mkdir src/models/multilingual-sentiment


RUN curl -L https://huggingface.co/lxyuan/distilbert-base-multilingual-cased-sentiments-student/resolve/main/config.json?download=true -o /src/models/multilingual-sentiment/config.json

RUN curl -L https://huggingface.co/lxyuan/distilbert-base-multilingual-cased-sentiments-student/resolve/main/tokenizer.json?download=true -o /src/models/multilingual-sentiment/tokenizer.json

RUN curl -L https://huggingface.co/lxyuan/distilbert-base-multilingual-cased-sentiments-student/resolve/main/pytorch_model.bin?download=true -o /src/models/multilingual-sentiment/pytorch_model.bin


CMD uvicorn app:app --host 0.0.0.0 --port ${PORT}
