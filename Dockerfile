FROM python:3.13.2-slim

# Set working directory to the *parent* of 'app'
WORKDIR /app

# Copy everything into container
COPY . .

# Make sure Python can see /app as a package
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose port for Streamlit
EXPOSE 8501

# Run Streamlit with the module path
CMD ["streamlit", "run", "app/app.py", "--server.headless=true"]
