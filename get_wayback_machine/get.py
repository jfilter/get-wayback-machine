import get_retries


def get(url, **kwargs):
    response = get_retries.get(
        f"http://archive.org/wayback/available?url={url.split('?')[0]}", **kwargs)

    if not response or response.status_code != 200:
        return None

    r_json = response.json()

    if not 'closest' in r_json['archived_snapshots']:
        return None

    clo = r_json['archived_snapshots']['closest']
    if clo['status'] != '200':
        return None

    response_final = get_retries.get(clo['url'])
    if not response_final or response_final.status_code != 200:
        return None
    return response_final
