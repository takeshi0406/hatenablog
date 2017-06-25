# hatenablog

A Python wrapper for HatenaBlog(はてなブログ)'s API.

http://developer.hatena.ne.jp/ja/documents/blog/apis/atom

## Instollation

Install from PyPI.

```bash
pip install hatenablog
```

Install from github.

```bash
pip install git+https://github.com/takeshi0406/hatenablog
```

## Usage

```python
from hatenablog import Client

client = Client(
    client_key='',
    client_secret='',
    resource_owner_key='',
    resource_owner_secret=''
    )

client.post_entries(
    user='takeshi0406',
    blog='kiito.hatenablog.com',
    title='Pythonで記事を更新します',
    body='記事の内容を記述します',
    categories=['テスト投稿'], # optional
    draft=True # optional
    )
```

## TODO

only post_entries method was impremented.
