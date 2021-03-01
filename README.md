# sendgrify

> SendGrid for Humans

**Sendgrify** is a Python package serving as a wrapper over the email delivery service [SendGrid](https://sendgrid.com/).

This is an attempt to simplify the use of [sendgrid-python](https://github.com/sendgrid/sendgrid-python): the Official Twilio SendGrid Led, Community Driven Python API Library.

## Installation

```console
$ pip install sendgrify
```

## Usage

### Initialization

Prior to use the package you should get a [SendGrid API key](https://sendgrid.com/docs/ui/account-and-settings/api-keys/).

```python
from sendgrify.core import SendGrid

sg = Sendgrid(api_key='your_sendgrid_api_key',
              from_addr='from@example.com',
              from_name='Sendgrify')
```

### Sending simple email

```python
sg.send(to='to@example.com',
        subject='Sendgrify is nice',
        msg='Hi there!\nI am using this cool new Python package')
```

### Sending to several recipients

```python
sg.send(to=['one@example.com', 'two@example.com'],
        subject='Sendgrify is nice',
        msg='Hi there!\nI am using this cool new Python package')
```

### Sending with carbon copy

```python
sg.send(to='to@example.com',
        cc=['one@example.com', 'two@example.com'],
        subject='Sendgrify is nice',
        msg='Hi there!\nI am using this cool new Python package')
```

### Sending with blind carbon copy

```python
sg.send(to='to@example.com',
        bcc=['one@example.com', 'two@example.com'],
        subject='Sendgrify is nice',
        msg='Hi there!\nI am using this cool new Python package')
```

### Sending with attachments

```python
sg.send(to='to@example.com',
        subject='Sendgrify is nice',
        msg='Hi there!\nI am using this cool new Python package',
        attachments=['README.md', 'system.zip'])
```

> Set the proper path to your attachments.

### Sending with html contents

```python
sg.send(to='to@example.com',
        subject='Sendgrify is nice',
        msg='Hi <b>there</b>!<br><br>I am using this <a href="https://pypi.org/">cool new Python package</a>',
        html=True)
```

## Changelog

| 1.0.0 | 01/03/2021 |
| ----- | ---------- |

- Add initial code.
- Add documentation.
- Add tests.
- Add makefile.
