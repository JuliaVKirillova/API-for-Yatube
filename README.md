# API for Yatube project with documentation

## Задача: Реализовать API для всех моделей проекта Yatube

### Ресурсы API Yatube
- Ресурс TOKEN: аутентификация.
- Ресурс USERS: пользователи.
- Ресурс POSTS: посты.
- Ресурс COMMENTS: комментарии к отзывам. Комментарий привязан к определённому отзыву.
- Ресурс GROUP: группы, по которым объединяются посты.
- FOLLOW: подписчики.

Виды запросов: GET, POST, PUT(PATCH), DELETE.

Документация создана на Redoc.

--- 

### Технологии:
- Python
- Django
- DRF
- Generic Views, Viewsets
- Token Authentication (JWTAuthentication)
- Pagination
- DjangoFilterBackend, SearchFilter, OrderingFilter
- Postman
