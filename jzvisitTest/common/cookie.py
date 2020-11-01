def cookie_to_selenium_format(cookie):
    cookie_selenium_mapping = {'path': '', 'secure': '', 'name': '', 'value': ''}
    cookie_dict = {}
    if getattr(cookie, 'domain_initial_dot'):
        cookie_dict['domain'] = getattr(cookie, 'domain')
    else:
        cookie_dict['domain'] = getattr(cookie, 'domain')
    for k in list(cookie_selenium_mapping.keys()):
        key = k
        value = getattr(cookie, k)
        cookie_dict[key] = value
    return cookie_dict
