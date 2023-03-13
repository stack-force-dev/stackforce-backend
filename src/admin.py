import secrets

from fastapi import HTTPException
from sqladmin import ModelView
from sqladmin.models import ModelViewMeta
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request

from src.app.claim.models import *
from src.config.settings import settings


from uuid import UUID


class MyBackend(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        if not all([
                form["username"] == settings.ADMIN_USERNAME,
                form["password"] == settings.ADMIN_PASSWORD]):
            raise HTTPException(status_code=403, detail="Invalid credentials!")
    
        request.session.update({"token": f"Bearer {secrets.token_hex(16)}"})
        return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        return "token" in request.session


def get_auth_backend():
    return MyBackend(settings.SECRET_KEY)


class MyView(ModelView, metaclass=ModelViewMeta):
    page_size = settings.ADMIN_PAGE_SIZE


class ClaimAdmin(MyView, model=Claim):
    column_list = [
        Claim.id,
        Claim.email,
        Claim.phone,
        Claim.message,
        Claim.created_at,
        Claim.updated_at
    ]
    column_sortable_list = [
        Claim.id,
        Claim.email,
        Claim.phone,
        Claim.message,
        Claim.created_at,
        Claim.updated_at
    ]
    column_searchable_list = [
        Claim.email,
        Claim.phone,
        Claim.message,
    ]


def init_models(admin):
    admin.add_view(ClaimAdmin)

