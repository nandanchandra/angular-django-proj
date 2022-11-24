from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    handler={
        'ValidationError': _handle_generic_error,
        'Http404': _handle_not_found_error,
        'PermissionDenied': _handle_permissiondenied_error,
        'NotAuthenticated': _handle_authentication_error
    }

    response = exception_handler(exc, context)

    exception_class = exc.__class__.__name__

    if exception_class in handler:
        return handler[exception_class](exc,context,response)
    return response

def _handle_not_found_error(exc, context, response):
    view = context.get("view", None)

    if view and hasattr(view, "queryset") and view.queryset is not None:
        error_key = view.queryset.model._meta.verbose_name
        response.data = {
            'message': 'Not Found',
            'errors': {error_key: response.data["detail"]},
        }
    else:
        response = _handle_generic_error(exc, context, response)
    return response


def _handle_authentication_error(exc,context,response):
    response.data={
            'errors' : {"details": "Authentication error"},
            'message': 'Authentication failed',
        }
    return response

def _handle_permissiondenied_error(exc,context,response):
    response.data={
            'errors' : {"details": "Permission error"},
            'message': 'Permission Denied',
        }
    return response

def _handle_generic_error(exc,context,response):
    response.data={
            'errors' :{"details":exc.detail},
            'message': "Bad request",
        }
    return response