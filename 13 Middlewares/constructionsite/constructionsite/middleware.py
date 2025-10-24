from django.http import HttpResponse
from django.conf import settings
import logging

class ConstructionSiteMiddleware:
    """
    Middleware to display a maintenance page if the site is under construction.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if getattr(settings, 'SITE_UNDER_CONSTRUCTION', False):
            return HttpResponse(
                "<html><body><h1>Site Under Construction</h1><p>We are currently working on the site. Please check back later.</p></body></html>",
                content_type="text/html",
                status=503
            )
        response = self.get_response(request)
        return response


class FooterAppendMiddleware:
    """
    Middleware to append a footer to all HTML responses.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if 'text/html' in response.get('Content-Type', ''):
            footer = "\n<footer><p>© 2025 Construction Site. All rights reserved.</p></footer>\n"
            content = response.content.decode('utf-8') + footer
            response.content = content.encode('utf-8')
            response['Content-Length'] = len(response.content)
        return response

import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

class ExceptionLoggingMiddleware:
    """
    Middleware that logs exceptions and handles them gracefully.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            # 👇 Middleware intentionally triggers exception for one route
            if request.path == '/test-exception/':
                raise RuntimeError("Triggered middleware exception for testing")

            response = self.get_response(request)
            return response

        except ValueError as e:
            logger.error(f"ValueError occurred: {e}")
            return HttpResponse(f"⚠️ ValueError: {e}", status=400)

        except Exception as e:
            logger.exception("Unhandled exception caught by middleware")
            return HttpResponse(
                "🚨 Middleware caught an unexpected error. Please try again later.",
                status=500,
            )


# http://127.0.0.1:8000/test-exception/ to raise error