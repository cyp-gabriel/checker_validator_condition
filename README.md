## v1.0

### main2.py, bc/tools.py

* Added condition function.
* Created full pre-condition, process, post-condition composition working:

```python
pre = condition(
        validator("arg must be positive", is_positive),
        validator("arg must not be zero", is_not_zero))

    sqr_cmd = partial(pre, sqr)

    post = condition(
        validator("result must be greater than 10", greaterThan(10)),
        validator("result must be less than 100", lessThan(100)))

    c = (Compose(sqr_cmd).then(partial(post, _identity)))

    print(c(3))
```
