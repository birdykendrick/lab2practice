import bmi

def test_findminmax():
    #Act
    minmax = [10,20,30,40,50]

    #arrange
    result = bmi.find_min_max(minmax)

    #assert
    assert result == [10,50]

def test_average():
    #act
    findavg = [10,20,30,40,50]

    #arrange
    result = bmi.calc_average(findavg)

    #assert
    assert result == 30

def test_median():
    #act
    findmed = [10,20,30,40,50]

    #arrange
    result = bmi.calc_median_temperature(findmed)

    #assert
    assert result == 30