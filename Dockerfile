FROM python:3-onbuild

EXPOSE 5000

CMD ["python", "./get.py"]

CMD ["python", "./send.py"]

CMD ["python", "./server.py"]