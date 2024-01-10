FROM python:3

WORKDIR /app

COPY app_requirement.txt /app/

RUN pip3 install --no-cache-dir -r app_requirement.txt

COPY . .

ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD [ "flask", "run" ]


