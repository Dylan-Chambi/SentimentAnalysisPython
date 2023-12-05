FROM python:3.11
ARG OPENAI_KEY
ENV OPENAI_KEY=$OPENAI_KEY
ENV PORT 8000

COPY requirements.txt /
RUN pip install -r requirements.txt

RUN python -m spacy download es_core_news_md


COPY ./src /src

RUN rm -rf /src/models/multilingual-sentiment

RUN mkdir /src/models/multilingual-sentiment

COPY app.py /app.py


RUN curl -L https://huggingface.co/lxyuan/distilbert-base-multilingual-cased-sentiments-student/resolve/main/config.json?download=true -o /src/models/multilingual-sentiment/config.json

RUN curl -L https://huggingface.co/lxyuan/distilbert-base-multilingual-cased-sentiments-student/resolve/main/tokenizer.json?download=true -o /src/models/multilingual-sentiment/tokenizer.json

RUN curl -L https://huggingface.co/lxyuan/distilbert-base-multilingual-cased-sentiments-student/resolve/main/pytorch_model.bin?download=true -o /src/models/multilingual-sentiment/pytorch_model.bin


CMD uvicorn app:app --host 0.0.0.0 --port 8000
