"""
TAGME restful API
"""
import urllib

TAGME_TAG_URL = "http://tagme.di.unipi.it/tag"


def tag(text, key, **kwargs):
    """Run the TAGME tag service and return a response object"""
    param = {"text": text, "key": key}
    for attr in (
        "lang",
        "tweet",
        "include_abstract",
        "include_categories",
        "include_all_spots",
        "long_text",
        "epsilon",
    ):
        if attr in kwargs and kwargs[attr] is not None:
            val = kwargs[attr]
            param[attr] = str(val).lower() if isinstance(val, bool) else str(val)
    # FIXME: dirty fix
    for k, v in param.items():
        param[k] = v.encode("utf8")
    data = urllib.parse.urlencode(param).encode("utf-8")
    request = urllib.request.Request(TAGME_TAG_URL, data)
    return urllib.request.urlopen(request).read().decode("utf-8")
