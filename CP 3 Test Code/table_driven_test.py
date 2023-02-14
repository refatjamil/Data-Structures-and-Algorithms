def avg(L):
    if not L:
        return None
    return sum(L)/len(L)

def test_avg():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [1, 2, 3],
            "expected": 2.0
        },
        {
            "name": "simple case 2",
            "input": [1, 2, 3, 4],
            "expected": 2.5
        },
        {
            "name": "list case 2",
            "input": [1, 2, 3],
            "expected": 2.0
        },
        {
            "name": "empty list",
            "input": [],
            "expected": None
        },
    ]

    for test_case in test_cases:
        assert test_case["expected"] == avg(test_case["input"]), test_case["name"]