FROM python:3
ADD server.py /
CMD [ "python", "./server.py" ]
ADD send.py /
CMD [ "python", "./send.py" ]
ADD get.py /
CMD [ "python", "./get.py" ]