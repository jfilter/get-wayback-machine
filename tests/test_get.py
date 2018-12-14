import get_wayback_machine


def test_success():
    res = get_wayback_machine.get(
        'https://tvline.com/2016/04/18/stana-katic-leaving-castle-season-9-beckett-dies/', max_backoff=64)
    assert(res.status_code == 200)


def test_fail():
    res = get_wayback_machine.get(
        'https://tvlineXXXX.com/2016/04/18/stana-katic-leaving-castle-season-9-beckett-dies/')
    assert(res is None)
