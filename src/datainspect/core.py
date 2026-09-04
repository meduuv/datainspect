from collections import Counter
import json

def json_stats(text:str):
    value=json.loads(text)
    if isinstance(value,list): return {"type":"array","items":len(value)}
    if isinstance(value,dict): return {"type":"object","keys":len(value),"names":sorted(value)[:20]}
    return {"type":type(value).__name__}

def frequencies(values):
    return Counter(values)
