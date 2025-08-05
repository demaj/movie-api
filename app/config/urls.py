from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path(r"admin/", admin.site.urls),
    path(r"accounts/", include("allauth.urls")),
    path(r"healthcheck/", include("healthcheck.urls"), name="healthcheck"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    path(r"api/", include("core.urls")),
    path(r"api-auth/", include("rest_framework.urls")),
    path(r"api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(r"api/docs/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path(r"api/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
]

if settings.DEBUG:
    urlpatterns += [
        path(
            r"400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request")},
        ),
        path(
            r"403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied!")},
        ),
        path(
            r"404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found!")},
        ),
        path(r"500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [path(r"__debug__/", include(debug_toolbar.urls))]
