#Django中POST请求 403 FORBIDDEN

```
To enable CSRF protection for your views, follow these steps:

1. Add the middleware`django.middleware.csrf.CsrfViewMiddleware` to your list ofmiddleware classes in `setting.py`, MIDDLEWARE_CLASSES. (It should comebefore any view middleware that assume that CSRF attacks havebeen dealt with.)

Alternatively, you can use the decorator `@csrf_protect` on particular viewsyou want to protect (see below).
```
(我尝试了`@csrf_exempt`也可以呢![](http://mat1.gtimg.com/www/mb/images/face/13.gif))
`8`过`@csrf_exempt`的作用是对当前view方法关闭CSRF

2. In any template that uses a POST form, use the csrf_token tag insidethe <form> element if the form is for an internal URL, e.g.:

`<form action="." method="post">{% csrf_token %}`
This should not be done for POST forms that target external URLs, sincethat would cause the CSRF token to be leaked, leading to a vulnerability.
```

```
3. In the corresponding view functions, ensure that the`django.core.context_processors.csrf` context processor isbeing used. Usually, this can be done in one of two ways:

Use RequestContext, which always uses`django.core.context_processors.csrf` (no matter what yourTEMPLATE_CONTEXT_PROCESSORS setting). If you are usinggeneric views or contrib apps, you are covered already, since theseapps use RequestContext throughout.

Manually import and use the processor to generate the CSRF token andadd it to the template context. e.g.:

from django.core.context_processors import csrf
from django.shortcuts import render_to_response

def my_view(request):
    c = {}
    c.update(csrf(request))
    # ... view code here
    return render_to_response("a_template.html", c)
You may want to write your ownrender_to_response() wrapper that takes careof this step for you.

The utility script extras/csrf_migration_helper.py can help to automate thefinding of code and templates that may need these steps. It contains full helpon how to use it.
```

网上大多说使用前两种方法可以解决问题，但第三种情况还是值得注意下。

附官方文档地址：https://docs.djangoproject.com/en/dev/ref/contrib/csrf/

