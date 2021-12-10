import app
from census import Census


# unit test jsonate function
def test_jsonate():
    header = 'h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13'
    c1 = Census(header, 'val1.1,val1.2,val1.3,val1.4,val1.5,val1.6,val1.7,val1.8,val1.9,val1.10,val1.11,val1.12,val1.13')
    c2 = Census(header, 'val2.1,val2.2,val2.3,val2.4,val2.5,val2.6,val2.7,val2.8,val2.9,val2.10,val2.11,val2.12,val2.13')
    data = [c1, c2]
    output = app.jsonate_data(data, 1, 1)
    assert output[1] == 200


# unit test bad request response
def test_bad_request():
    output = app.bad_request(400)
    assert output[1] == 400


# unit test for valid age
def test_is_valid_age():
    header = 'h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13'
    c1 = Census(header,
                '51,val1.2,val1.3,val1.4,val1.5,val1.6,val1.7,val1.8,val1.9,val1.10,val1.11,val1.12,val1.13')
    flag = app.is_valid_age('over50', c1)
    assert flag


# negative unit test for valid age
def test_negative_is_valid_age():
    header = 'h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13'
    c1 = Census(header,
                '49,val1.2,val1.3,val1.4,val1.5,val1.6,val1.7,val1.8,val1.9,val1.10,val1.11,val1.12,val1.13')
    flag = app.is_valid_age('over50', c1)
    assert not flag


# unit test for valid education
def test_is_valid_education():
    header = 'h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13'
    c1 = Census(header,
                '51,val1.2,val1.3,Masters,val1.5,val1.6,val1.7,val1.8,val1.9,val1.10,val1.11,val1.12,val1.13')
    flag = app.is_valid_education('master', c1)
    assert flag


# negative unit test for valid education
def test_negative_is_valid_education():
    header = 'h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13'
    c1 = Census(header,
                '51,val1.2,val1.3,Bachelors,val1.5,val1.6,val1.7,val1.8,val1.9,val1.10,val1.11,val1.12,val1.13')
    flag = app.is_valid_education('master', c1)
    assert not flag


# unit test for valid country
def test_is_valid_country():
    header = 'h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13'
    c1 = Census(header,
                '51,val1.2,val1.3,Masters,val1.5,val1.6,val1.7,val1.8,val1.9,val1.10,Mexico,val1.12,val1.13')
    flag = app.is_valid_country('mex', c1)
    assert flag


# negative unit test for valid country
def test_negative_is_valid_country():
    header = 'h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13'
    c1 = Census(header,
                '51,val1.2,val1.3,Masters,val1.5,val1.6,val1.7,val1.8,val1.9,val1.10,Canada,val1.12,val1.13')
    flag = app.is_valid_country('mex', c1)
    assert not flag

