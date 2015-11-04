from django.contrib.auth import user_logged_in, _get_user_session_key
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect, HttpResponse
from django.middleware.csrf import rotate_token
from django.shortcuts import resolve_url
from django.contrib.auth.forms import AuthenticationForm
from django.template.response import TemplateResponse
from django.utils.functional import SimpleLazyObject
from django.utils.http import is_safe_url
from bson.objectid import ObjectId
from mongoengine.django.auth import get_user
from gestionCJN import settings

SESSION_KEY = '_auth_user_id'
BACKEND_SESSION_KEY = '_auth_user_backend'
HASH_SESSION_KEY = '_auth_user_hash'
REDIRECT_FIELD_NAME = 'next'


class AuthenticationMiddleware(object):
    def process_request(self, request):
        assert hasattr(request, 'session'), (
            "The Django authentication middleware requires session middleware "
            "to be installed. Edit your MIDDLEWARE_CLASSES setting to insert "
            "'django.contrib.sessions.middleware.SessionMiddleware' before "
            "'django.contrib.auth.middleware.AuthenticationMiddleware'."
        )
        request.user = SimpleLazyObject(lambda: get_user(_get_user_session_key(request)))


def _get_user_session_key(request):
    if SESSION_KEY in request.session:
        return ObjectId(request.session[SESSION_KEY])


def login(request, user):
    session_auth_hash = ''
    if user is None:
        user = request.user
    if hasattr(user, 'get_session_auth_hash'):
        session_auth_hash = user.get_session_auth_hash()

    if SESSION_KEY in request.session:
        if _get_user_session_key(request) != user.pk or (
                    session_auth_hash and
                        request.session.get(HASH_SESSION_KEY) != session_auth_hash):
            request.session.flush()
    else:
        request.session.cycle_key()

    request.session[SESSION_KEY] = user.pk
    request.session[BACKEND_SESSION_KEY] = user.backend
    request.session[HASH_SESSION_KEY] = session_auth_hash
    if hasattr(request, 'user'):
        request.user = user
    rotate_token(request)
    user_logged_in.send(sender=user.__class__, request=request, user=user)


def vista_login(request, template_name='registration/login.html',
                redirect_field_name=REDIRECT_FIELD_NAME,
                authentication_form=AuthenticationForm,
                current_app=None, extra_context=None):
    """
    Displays the login form and handles the login action.
    """
    redirect_to = request.POST.get(redirect_field_name,
                                   request.GET.get(redirect_field_name, ''))

    if request.method == "POST":
        form = authentication_form(request, data=request.POST)
        if form.is_valid():

            # Ensure the user-originating redirection url is safe.
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

            # Okay, security check complete. Log the user in.
            login(request, form.get_user())

            return HttpResponse('Login')
    else:
        form = authentication_form(request)

    current_site = get_current_site(request)

    context = {
        'form': form,
        redirect_field_name: resolve_url(settings.LOGIN_REDIRECT_URL),
        'site': current_site,
        'site_name': current_site.name,
    }
    if extra_context is not None:
        context.update(extra_context)

    if current_app is not None:
        request.current_app = current_app

    if redirect_to != '' and request.method == "GET":
        return HttpResponse('Unauthorized', status=401)

    return TemplateResponse(request, template_name, context)
