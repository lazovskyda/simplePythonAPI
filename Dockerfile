FROM python:3.9
ADD simple_api.py .
RUN pip install requests beautifulsoup4

CMD ["python", "./simple_api.py"]