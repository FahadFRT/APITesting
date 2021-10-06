from config import HEADERS, SESSION


class RequestClient:
    def get_req(self, url, headers=None, auth=(None, None), Authorization=None, qop=None, algorithm=None,
                stale_after=None, Accept=None, IF_MODIFIED_SINCE=None, IF_NONE_MATCH="test", CONTENT_TYPE=None,
                path_params=None, form_data=None, file=None):
        if auth == (None, None):
            auth = None
        else:
            pass
        response = SESSION.get(url, headers=HEADERS, auth=auth)
        return response
