python manage.py makemigrations
python manage.py migrate


python manage.py runserver


Примените разрешение к представлению:

python
Копировать код
class AdminOnlyView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    # ...

operation_summary="Register a new user",