# Pull official base image
FROM python:3.10-slim

# install requirements
COPY Pipfile.lock Pipfile ./
RUN pip install -U pip setuptools pipenv && pipenv install

# Add project files
COPY . .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]