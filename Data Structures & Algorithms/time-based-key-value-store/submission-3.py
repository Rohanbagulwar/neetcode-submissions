class TimeMap:

    def __init__(self):
        self.a = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.a:
            self.a[key] = {timestamp: value}
        else:
            self.a[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.a:
            return ""


        if timestamp in self.a[key]:
            return self.a[key][timestamp]

        valid_ts = []
        for ts in self.a[key]:
            if ts <= timestamp:
                valid_ts.append(ts)

        if not valid_ts:
            return ""

        return self.a[key][max(valid_ts)]
        
