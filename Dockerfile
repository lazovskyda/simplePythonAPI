FROM python:3.9
ADD simpleAPI.py .
RUN pip install requests beautifulsoup4

CMD ["python", "./simpleAPI.py"]