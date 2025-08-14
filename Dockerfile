FROM python:3.13.2-slim 
WORKDIR /app
COPY . /app
ENV PYTHONPATH=/app 
RUN pip install --upgrade pip && pip install -r requirements.txt 
EXPOSE 8501
CMD ["streamlit", "run", "app/app.py", "server.headless", "true"] 