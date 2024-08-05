from django.core.cache import cache
from rest_framework.response import Response


class CachedListMixin:
    cache_timeout = 60 * 15

    def get_cache_key(self):
        request = self.request
        return f"{request.get_full_path()}"

    def get(self, request, *args, **kwargs):

        cache_key = self.get_cache_key()
        cached_response = cache.get(cache_key)
        if cached_response:
            return Response(cached_response)
        response = super().get(request, *args, **kwargs)
        cache.set(cache_key, response.data, timeout=self.cache_timeout)
        return response
