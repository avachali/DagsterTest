from TestProject.ops.complex_job import {
    diamond,
    find_highest_calorie_cereal,
}


def test_find_highest_calorie_cereal():
    cereals = [
        {"name": "hi-cal cereal", "calories": 400},
        {"name": "lo-cal cereal", "calories": 50},
    ]
    result = find_highest_calorie_cereal(cereals)
    assert result == "hi-cal cereal"


def test_diamond():
    res = diamond.execute_in_process()
    assert res.success
    assert res.output_for_node("find_highest_protein_cereal") == "Special K"
