from datetime import datetime, timezone

import ntplib


def utcnow_timeserver():
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request("pool.ntp.org")
    now = datetime.fromtimestamp(response.tx_time, tz=timezone.utc)
    return now
