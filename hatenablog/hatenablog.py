import xmltodict
from collections import OrderedDict
from requests_oauthlib import OAuth1Session
from typing import List, Optional


class Client(OAuth1Session):
    ENDPOINT = 'https://blog.hatena.ne.jp/{user}/{blog}/atom/entry'

    def __init__(self, client_key: str,
                 client_secret: str,
                 resource_owner_key: str,
                 resource_owner_secret: str):
        """
        Initialize class instance.

        Args:
            client_key: client key.
            client_secret: client secret.
            resource_owner_key: resource owner key.
            resource_owner_secret: resource owner secret.

        """
        super().__init__(
            client_key=client_key,
            client_secret=client_secret,
            resource_owner_key=resource_owner_key,
            resource_owner_secret=resource_owner_secret
        )

    def post_entries(self, user: str, blog: str,
                     title: str, body: str,
                     categories: List[str]=[],
                     draft: bool=False) -> OrderedDict:
        """
        Args:
            user: hatena user name.
            blog: blog url (eg. 'http://xxxxxxx.hatenablog.com').
            title: article title.
            body: article body.
            categories (optional): article categories.
            draft (optional): if true

        Returns:
            API response

        Raises:
            raise API Error

        """
        url = self.ENDPOINT.format(user=user, blog=blog)
        xml = _create_body_xml(title, body, categories, draft)
        res = self.post(url, data=xml)
        _assert_response_ok(res)
        return _parse_response(res.text)


def _create_body_xml(
        title: str, body: str, categories: List[str], draft: bool) -> str:
    body = {
        'entry': {
            '@xmlns': 'http://www.w3.org/2005/Atom',
            '@xmlns:app': 'http://www.w3.org/2007/app',
            'title': title,
            'author': {'name': 'name'},
            'content': {
                '@type': 'text/plain',
                '#text': body
            },
            'category': _create_categories(categories),
            'app:control': {
                'app:draft': _is_draft(draft)
            }
        }
    }
    return xmltodict.unparse(body).encode('utf-8')


def _create_categories(categories: List[str]) -> Optional[List[dict]]:
    if not categories:
        return None
    return [{'@term': c} for c in categories]


def _is_draft(draft: bool) -> str:
    return 'yes' if draft else 'no'


def _assert_response_ok(response):
    if not response.ok:
        response.raise_for_status()


def _parse_response(response_text: str) -> OrderedDict:
    return xmltodict.parse(response_text)
