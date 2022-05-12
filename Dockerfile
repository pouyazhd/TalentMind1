FROM python
WORKDIR /home/app
COPY . .
RUN pip install -r requirement.txt
CMD ["python","main.py"]