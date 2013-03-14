from miranda import upnp

conn = upnp()


def _send(host, action, args=None):
    if not args:
        args = {}
    event = 'http://'+host+'/upnp/control/basicevent1'
    resp = conn.sendSOAP(
        host,
        'urn:Belkin:service:basicevent:1',
        event,
        action,
        args
    )
    return resp


def toggle(host):
    if get(host):
        off(host)
    else:
        on(host)


def get(host):
    """
    Gets the value of the first switch that it finds
    """
    resp = _send(host, 'GetBinaryState')
    tagValue = conn.extractSingleTag(resp, 'BinaryState')
    return True if tagValue == '1' else False


def on(host):
    """
    Turns on the first switch that it finds.

    BinaryState is set to 'Error' in the case that it was already on.
    """
    resp = _send(host, 'SetBinaryState', {'BinaryState': (1, 'Boolean')})
    tagValue = conn.extractSingleTag(resp, 'BinaryState')
    return True if tagValue in ['1', 'Error'] else False


def off(host):
    """
    Turns off the first switch that it finds.

    BinaryState is set to 'Error' in the case that it was already off.
    """
    resp = _send(host, 'SetBinaryState', {'BinaryState': (0, 'Boolean')})
    tagValue = conn.extractSingleTag(resp, 'BinaryState')
    return True if tagValue in ['0', 'Error'] else False
