# sendgrify

SendGrid for Humans.

**Sendgrify** is a Python package serving as a wrapper over the email delivery service [SendGrid](https://sendgrid.com/).

This is an attempt to simplify the use of [sendgrid-python](https://github.com/sendgrid/sendgrid-python): the Official Twilio SendGrid Led, Community Driven Python API Library.

> Sending emails, the easy way!

## Installation

```console
$ pip install sendgrify
```

## Usage

1. Grab your [SendGrid API Key](https://docs.sendgrid.com/ui/account-and-settings/api-keys).
2. Code!

```python
>>> from sendgrid import SendGrid
>>> handler = SendGrid('YOUR_SENDGRID_API_KEY', 'from_addr@example.com', 'From Name')
>>> handler.send(to='hello@example.com', subject='Hi there', msg='This is just a test')
```

### Advanced usage

Function `send()` also admits some more parameters:

- `cc`: as a list of emails for carbon copy.
- `bcc`: as a list of emails for blind carbon copy.
- `attachments`: as a list of paths for file attachments.
- `as_markdown`: as a boolean (if True msg will be rendered from Markdown).

## Tests

```console
$ pip install -r requirements-dev.txt
$ pytest
```

## License

MIT
