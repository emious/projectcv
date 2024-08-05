## Use the official Python image from the Docker Hub
#FROM python:3.11
#
## Set environment variables
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#
## Set work directory
#WORKDIR /app
#
## Install dependencies
#COPY requirements.txt /app/
#RUN pip install --no-cache-dir -r requirements.txt
#
## Copy project
#COPY . /app/
#
## Expose port 8000 for the app
#EXPOSE 8000
#
## Run the Django development server
#CMD ["uvicorn", "projectcv.asgi:application", "--host", "0.0.0.0", "--port", "8000"]

# استفاده از تصویر پایه
FROM python:3.11-alpine



# تنظیم دایرکتوری کاری
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt


# کپی کردن فایل‌های پروژه به دایرکتوری کاری
COPY . /app/

# نصب وابستگی‌ها




EXPOSE 8000


#COPY entrypoint.sh /app/entrypoint.sh
#RUN chmod +x /app/entrypoint.sh
#
## تنظیم اسکریپت به‌عنوان نقطه ورود کانتینر
#ENTRYPOINT ["/app/entrypoint.sh"]
# فرمان پیش‌فرض
#CMD ["uvicorn", "projectcv.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
