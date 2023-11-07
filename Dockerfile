FROM python:3.9

WORKDIR /usr/app/src

RUN pip install streamlit

COPY / ./

CMD ["streamlit","run","main.py"]