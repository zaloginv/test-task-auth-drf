# test-task-auth-drf

**Стэк**: drf, django-allauth, simplejwt

**Задача**: Реализовать регистрацию через google, с использованием jwt токенов для дальнейшей аутентификации пользователя на сайте. 

При переходе на /auth/google/ пользователя редиректит на страницу авторизации google, после успешного входа пользователю в теле ответа возвращается 
access и refresh токен и сохранятеся в бд. 

Создать примитивную модель для сохранения пользователя в бд. Создать сериализатор (любой) для проверки. Навесить на него 
permission_classes = (IsAuthenticatedOrReadOnly,). 