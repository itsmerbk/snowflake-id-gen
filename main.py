class Snowflake:
    def __init__(self, worker_id):
        self.worker, self.seq, self.last_ts = worker_id & 0x3FF, 0, -1
    def next_id(self, ts_ms):
        if ts_ms == self.last_ts: self.seq = (self.seq + 1) & 0xFFF
        else: self.seq = 0; self.last_ts = ts_ms
        return (ts_ms << 22) | (self.worker << 12) | self.seq

if __name__ == "__main__":
    sf = Snowflake(7)
    id1, id2 = sf.next_id(1700000000), sf.next_id(1700000000)
    assert id2 > id1
    print("[PASS] 040_snowflake_id_gen")
