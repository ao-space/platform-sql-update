FROM python:3.7-slim-bullseye
WORKDIR /opt/app
COPY entrypoint.py entrypoint.py
RUN pip install mysql-connector-python -i https://pypi.tuna.tsinghua.edu.cn/simple
CMD python3 /opt/app/entrypoint.py