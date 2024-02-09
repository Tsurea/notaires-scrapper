FROM python:3.12

WORKDIR /usr/bin/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install && playwright install-deps

COPY . .

RUN mkdir output

CMD ["python",	"./srcs/run.py",  "https://www.notaires.fr/fr/annuaire/ile-de-france/paris"]
