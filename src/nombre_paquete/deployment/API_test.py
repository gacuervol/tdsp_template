import requests
# 
features = [2009.021484, 0.0200, 1.000000, 0.960000, 0.000000, 14785.913267, -334.182204]
r = requests.post('http://127.0.0.1:8000/predict', json={
    "features_7": features
    })
print(r.json()) # 