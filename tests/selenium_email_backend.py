import os
from typing import Any

from django.conf import settings
from collections.abc import Iterable
from django.core.mail.backends.base import BaseEmailBackend
from django.core.mail.message import EmailMessage



class SeleniumEmailBackend(BaseEmailBackend):
    def __init__(self, fail_silently: bool = ..., **kwargs: Any) -> None:
        super().__init__(fail_silently, **kwargs)
        self._fpath  = getattr(settings, 'EMAIL_FILE_PATH', None)
        # pokud je self._path = None vzhodi vyjimku
        self._filename = 'selenium_confirm_email.txt'
        os.makedirs(self._fpath, exist_ok=True)
        
    def send_messages(self, email_messages: Iterable[EmailMessage]) -> None:
        with open(os.path.join(self._fpath, self._filename), "w") as message:
            message.write(email_messages[0].body)
        return None
    