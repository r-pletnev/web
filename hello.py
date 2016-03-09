def app(env, start_response):
    # import pdb; pdb.set_trace()
    data = '\n'.join(env['QUERY_STRING'].split('&'))
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data))),
        ('Connection', 'Keep-Alive'),
        ('Keep-Alive', '600'),
    ]
    start_response(status, response_headers)
    return iter([data])

