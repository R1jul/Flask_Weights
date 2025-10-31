from code2 import code2

def test_kg_lb():
    client=code2.code2.test_client()
    resp=client.get("/convert?value=1&unit=kg")
    assert b"2.20 lb" in resp.data
    
def test_lb_kg():
    client=code2.code2.test_client()
    resp=client.get("/convert?value=2.20&unit=lb")
    assert b"1.00 kg" in resp.data