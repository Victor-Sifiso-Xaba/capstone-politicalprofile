"""
Views for the politicalprofile Django application.

This module contains view functions responsible for rendering
pages related to political profiles and values.
"""

from django.shortcuts import render

def index_page(request):
    """
    Render the main index page of the application.

    Args:
        request: Django HttpRequest object.

    Returns:
        HttpResponse rendering the index.html template.
    """
    return render(request, "index.html")

def values_view(request):
    """
    Render the values page for the political profile.

    Args:
        request: Django HttpRequest object.

    Returns:
        HttpResponse rendering the values.html template.
    """
    return render(request, "politicalprofile/values.html")
