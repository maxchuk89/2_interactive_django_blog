from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # твой блог с namespace 'blog'
    path('', include(('blog.urls', 'blog'), namespace='blog')),
]

# Подключаем маршруты тулбара ТОЛЬКО в DEBUG
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
