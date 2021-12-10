import json
import logging.config
import os
from flask import Flask, request, Request, Response

from census import Census

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(name)s %(levelname)s:%(message)s')
log = logging.getLogger(__name__)


@app.route('/census_income', methods=['GET'])
# return census income data
def get_census_income():
    # census data header
    header_string = None
    # census data chunk (10 records per page due to front-end loading performance)
    census = []
    collection = []
    # obtain query parameters
    file_name = request.args.get('file_name')
    # check rank parameter value
    rank_value = request.args.get('rank').strip()
    rank_value_length = len(rank_value)
    # check age parameter value
    age = request.args.get('age')
    # check education parameter value
    education = request.args.get('education')
    # check country parameter value
    country = request.args.get('country')
    # total pages by 10
    pages = 0
    # assign rank value and file object if rank value is numeric and not blank
    if rank_value_length > 0 and rank_value.isdigit():
        index = int(rank_value)
        # initialize given csv file object
        if os.path.exists(file_name + '.csv'):
            file_obj = open(file_name + '.csv', 'r')
        else:
            file_obj = None
    else:
        # invalid cases
        index = -1
        file_obj = None
    try:
        if index >= 0 and file_obj is not None:
            # fetch data from data source from record rank up to 10 records
            rank = -1
            for record in file_obj:
                # collect record header
                if rank == -1:
                    header_string = record
                # collect next 10 records starting from given rank
                if rank > -1:
                    census_rec = Census(header_string, record)
                    # log.info(census_rec.to_string())
                    age_flag = is_valid_age(age, census_rec)
                    education_flag = is_valid_education(education, census_rec)
                    country_flag = is_valid_country(country, census_rec)
                    if age_flag and education_flag and country_flag:
                        collection.append(census_rec)
                rank += 1
            count = 0
            for record in collection:
                if count >= index and len(census) < 10:
                    census.append(record)
                count += 1
            pages = int(len(collection) / 10)
            if pages * 10 >= index:
                page_num = int((index + 10) / 10)
            else:
                page_num = 1
            reminder = len(collection) % 10
            if reminder > 0:
                pages += 1
    except Exception as e:
        log.error(e)
        raise e
    finally:
        if file_obj is not None:
            file_obj.close()
    return jsonate_data(census, pages, page_num)


# jsonate given census data set with header info
# return the data set on JSON format
def jsonate_data(data, pages, page_num):
    # default response for callback
    output = {"records": [], "numRecords": 0, "pages": pages, "page": page_num}
    # record counter
    count = 0
    # record header should be valid to proceed
    if data is not None:
        # iterate records in given data set
        for census_data in data:
            data_block = census_data.get_json_block()
            output["records"].append(data_block)
            count += 1
        # populate the number of records
        output["numRecords"] = count
        response = json.dumps(output)
        resp = Response(response)
        resp.headers['Content-Type'] = 'application/json'
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp, 200
    else:
        return bad_request(400)


# return true if age choice is valid
def is_valid_age(age, census_rec):
    is_correct_pick = True
    if age != 'any':
        age_val = census_rec.get_age()
        if age == 'over50':
            if str(age_val).isdigit():
                if int(age_val) <= 50:
                    is_correct_pick = False
            else:
                is_correct_pick = False
        elif age == 'less50':
            if str(age_val).isdigit():
                if int(age_val) >= 50:
                    is_correct_pick = False
            else:
                is_correct_pick = False
        elif age == 'less30':
            if str(age_val).isdigit():
                if int(age_val) >= 30:
                    is_correct_pick = False
            else:
                is_correct_pick = False
    return is_correct_pick


# return true if education choice is valid
def is_valid_education(education, census_rec):
    is_correct_pick = True
    if education != 'any':
        education_val = census_rec.get_education()
        if education == 'bachelor':
            if education_val != 'Bachelors':
                is_correct_pick = False
        elif education == 'master':
            if education_val != 'Masters':
                is_correct_pick = False
        elif education == 'college':
            if education_val != 'Some-College':
                is_correct_pick = False
        elif education == 'grad':
            if education_val != 'HS-grad':
                is_correct_pick = False
    return is_correct_pick


# return true if country choice is valid
def is_valid_country(country, census_rec):
    is_correct_pick = True
    if country != 'any':
        country_val = census_rec.get_country()
        if country == 'us':
            if country_val != 'United-States':
                is_correct_pick = False
        elif country == 'can':
            if country_val != 'Canada':
                is_correct_pick = False
        elif country == 'mex':
            if country_val != 'Mexico':
                is_correct_pick = False
    return is_correct_pick


@app.errorhandler(400)
# 400 bad request output
def bad_request(error):
    err_output = {"message": "invalid input requested!", "numRecords": 0}
    response = json.dumps(err_output)
    resp = Response(response)
    resp.headers['Content-Type'] = 'application/json'
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp, error


if __name__ == '__main__':
    app.run()
