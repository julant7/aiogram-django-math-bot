from typing import Final

from app.apps.core.models import TGUser


class CoreUseCase:
    @staticmethod
    async def register_bot_user(
            user_id: int,
            chat_id: int,
            username: str | None,
    ) -> tuple[TGUser, bool]:
        return await TGUser.objects.aget_or_create(
            id=user_id,
            chat_id=chat_id,
            username=username,
        )


CORE_USE_CASE: Final[CoreUseCase] = CoreUseCase()
