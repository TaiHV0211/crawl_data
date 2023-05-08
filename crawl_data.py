import requests

import pandas as pd

import sqlalchemy
address = []
bedrooms = []
bathrooms = []
agent_name = []
aria_code = []
telephones = []
prices = []
final = {}
highrespath = []
medrespath = []
lowrespath = []
descriptions = []
id_root = []
for i in range(51):
    cookies = {
        'visid_incap_2269415': 'H3hhmIXnQH6GEIwuzi3RCK+tUGQAAAAAQUIPAAAAAACXVXzwM67B+o2wWggIKfrV',
        'nlbi_2269415': 'PNBLPDI+73oToxhR+/Ys1gAAAAAtiUhcOcbVAGZ3xGHw0/KW',
        'incap_ses_257_2269415': 'nl5EU8DegzVT/hmvkwyRA6+tUGQAAAAAJBNzmXWP2gBol8Z7tk+jdg==',
        'incap_ses_969_2269415': 'nmLKRHa6WmkvbtmcMZVyDbGtUGQAAAAAFhWWtZ+oDy3w+QLePHcbaQ==',
        '_gcl_au': '1.1.1673775659.1683008948',
        'reese84': '3:yeWqKdWehDKWeUBH4w4/sA==:p7+5ErgJmIhQHiKT9jhujF8Wz2OXCVQrxiMemy1CM6qbvet8vwary9AklsFuA8RC5tJYR9Q6qb7hdKhYEYhB+PGCa64kcWS0UNJMVnuyXr/GjfSlW4GVMMWvO5aJD3iommOEwW/KWD31/sdMIkW2xa6DXb6rgy+rcsFkgMdEaMVVVwIt015Na66ceVTmekYAHApgOV4keHkE3CHr74+w1OMEpURUoCfmU0SUv1TeFHYDoVYg97i/Y0+wXYLg3keJYVwsSPBR40q6vnCwiPaeuNwY5kTneywwIVM4e+W77IdqteBOg3tlCkShe3DYDitUfjt696SOGx5h172TrKVBcXoa77szEyvjDvOTV4WIQJR5+BCGWlHoiWz1Md98ghUvvwJDZxYSDjt4yCC4qI53EQ+P8BtnbDDsx4V7RUmu6tFumpOONX2YsUMoLVByI8x+3hH4l+3rrdey9/RdttEzHA==:CDI3sxHi+257JpAfpvs/f09LMUf2OQZZaHKe8VLwUXQ=',
        '_gid': 'GA1.2.1901394588.1683008948',
        'gig_bootstrap_3_mrQiIl6ov44s2X3j6NGWVZ9SDDtplqV7WgdcyEpGYnYxl7ygDWPQHqQqtpSiUfko': 'gigya-pr_ver4',
        'ASP.NET_SessionId': 'd5hqgno4wzfshpndjo0ax0er',
        'visid_incap_2271082': 'NsK0gReASJyZZI7mHyInhg+uUGQAAAAAQUIPAAAAAABYrxLllhWiQtHWpWwzVw9j',
        'nlbi_2271082': 'yBHnW/PjfjAp1pkaVPrQ3QAAAADfZyk/SYTXADXFmVHBf3jV',
        'incap_ses_969_2271082': 'QoikTNfHHXSkFdqcMZVyDRWuUGQAAAAAi0KQneULrrjnT1V1u6xGqg==',
        '_dc_gtm_UA-12908513-11': '1',
        'nlbi_2269415_2147483392': 'yzjoJIwFwgP9wpP8+/Ys1gAAAADBCH+WTRNvsH2vdckwrPYS',
        '_ga': 'GA1.2.1607348873.1683008948',
        '_ga_Y07J3B53QP': 'GS1.1.1683008947.1.1.1683009257.18.0.0',
        '_4c_': '%7B%22_4c_s_%22%3A%22jVTda9swEP9XisbyFLmSLH8F8lBSKIUWxtbtYS9Fkc6JqGMZWYnblf7vO3luUtYxmgdH%2Bt3d73Sfz2TYQksWPC9TxiqRlTIv5uQBnnqyeCbemvh3IAsihco5qIxmsqyp5GlKK0g1XRccapkKrteazMnjyJXljDOZyqyakxAashBZJdj4e5kT3U2kz0Q7A0jOq4TLhDNa98gRfo3%2BGB4778xeh%2Fvw1EW9AdZnvXlAgYGD1XA%2FWBO2KBBMlid0C3azDZFXlJHFdD7q4GmwrXHD32YTejTLRYHo2ruhh2i52nq3gzPOI4XDzJBbFYP1UIP3owreehviGz2oJjifaDVhmMwTTEf4RrWbvdqMocer22zAnF1jIUitmh4Q%2B%2BLdwbYa%2FnCv3L4NPvL8sBBatUPsK%2FTWQBusapxfud0OvNWqGX0dJTGHY%2Fnw0DgUR0Ks%2BBw%2FEe%2B8wfPVxf3368v4mpwVqSzLIk3%2BtERZjRna%2B8i7DaHrF%2BfnwzAkpzDPd6r79NO53Q0coFnK2Qpdg19mMsGil6L8LFa0qpKU55LlsxsVbNgbuFWPS3STyqrisxvXbo4oFQgj%2FkbXtkvBkzTn7K0uopQXWSKqosxm35wPy5xezjB1HfjwdIdNc%2BXdvru%2BXPIj%2Bg2U19souzZLNrvzqu2VDta1EyZmqz1WtdVPy9XFZSwijOJTERG78xZr5m8hbB3OCN6VsVFrTLmJygZqtW9CvMam0o3qe6sN9A%2FBdeTldVZSVmV5VmScTbNSYpqmSekO06TIt9pSsqzi77UnavraatD%2Bx168tz%2FY12GvlSm51iXlpi6oLGqcc1MyKti6znkqCybX5ETJOcMQWDpR8vL0ovq0PyqldZXTQtWCcg6aVszklAncLJrH7ZCSv16Jrv4RZftKeUrwR7aO7cJkOC07JlkRk%2F4h46PPD3l7efkN%22%7D',
        '_gali': 'ListViewPagination_Bottom',
    }

    headers = {
        'authority': 'api2.realtor.ca',
        'accept': '*/*',
        'accept-language': 'en,vi-VN;q=0.9,vi;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5,cy;q=0.4',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'visid_incap_2269415=H3hhmIXnQH6GEIwuzi3RCK+tUGQAAAAAQUIPAAAAAACXVXzwM67B+o2wWggIKfrV; nlbi_2269415=PNBLPDI+73oToxhR+/Ys1gAAAAAtiUhcOcbVAGZ3xGHw0/KW; incap_ses_257_2269415=nl5EU8DegzVT/hmvkwyRA6+tUGQAAAAAJBNzmXWP2gBol8Z7tk+jdg==; incap_ses_969_2269415=nmLKRHa6WmkvbtmcMZVyDbGtUGQAAAAAFhWWtZ+oDy3w+QLePHcbaQ==; _gcl_au=1.1.1673775659.1683008948; reese84=3:yeWqKdWehDKWeUBH4w4/sA==:p7+5ErgJmIhQHiKT9jhujF8Wz2OXCVQrxiMemy1CM6qbvet8vwary9AklsFuA8RC5tJYR9Q6qb7hdKhYEYhB+PGCa64kcWS0UNJMVnuyXr/GjfSlW4GVMMWvO5aJD3iommOEwW/KWD31/sdMIkW2xa6DXb6rgy+rcsFkgMdEaMVVVwIt015Na66ceVTmekYAHApgOV4keHkE3CHr74+w1OMEpURUoCfmU0SUv1TeFHYDoVYg97i/Y0+wXYLg3keJYVwsSPBR40q6vnCwiPaeuNwY5kTneywwIVM4e+W77IdqteBOg3tlCkShe3DYDitUfjt696SOGx5h172TrKVBcXoa77szEyvjDvOTV4WIQJR5+BCGWlHoiWz1Md98ghUvvwJDZxYSDjt4yCC4qI53EQ+P8BtnbDDsx4V7RUmu6tFumpOONX2YsUMoLVByI8x+3hH4l+3rrdey9/RdttEzHA==:CDI3sxHi+257JpAfpvs/f09LMUf2OQZZaHKe8VLwUXQ=; _gid=GA1.2.1901394588.1683008948; gig_bootstrap_3_mrQiIl6ov44s2X3j6NGWVZ9SDDtplqV7WgdcyEpGYnYxl7ygDWPQHqQqtpSiUfko=gigya-pr_ver4; ASP.NET_SessionId=d5hqgno4wzfshpndjo0ax0er; visid_incap_2271082=NsK0gReASJyZZI7mHyInhg+uUGQAAAAAQUIPAAAAAABYrxLllhWiQtHWpWwzVw9j; nlbi_2271082=yBHnW/PjfjAp1pkaVPrQ3QAAAADfZyk/SYTXADXFmVHBf3jV; incap_ses_969_2271082=QoikTNfHHXSkFdqcMZVyDRWuUGQAAAAAi0KQneULrrjnT1V1u6xGqg==; _dc_gtm_UA-12908513-11=1; nlbi_2269415_2147483392=yzjoJIwFwgP9wpP8+/Ys1gAAAADBCH+WTRNvsH2vdckwrPYS; _ga=GA1.2.1607348873.1683008948; _ga_Y07J3B53QP=GS1.1.1683008947.1.1.1683009257.18.0.0; _4c_=%7B%22_4c_s_%22%3A%22jVTda9swEP9XisbyFLmSLH8F8lBSKIUWxtbtYS9Fkc6JqGMZWYnblf7vO3luUtYxmgdH%2Bt3d73Sfz2TYQksWPC9TxiqRlTIv5uQBnnqyeCbemvh3IAsihco5qIxmsqyp5GlKK0g1XRccapkKrteazMnjyJXljDOZyqyakxAashBZJdj4e5kT3U2kz0Q7A0jOq4TLhDNa98gRfo3%2BGB4778xeh%2Fvw1EW9AdZnvXlAgYGD1XA%2FWBO2KBBMlid0C3azDZFXlJHFdD7q4GmwrXHD32YTejTLRYHo2ruhh2i52nq3gzPOI4XDzJBbFYP1UIP3owreehviGz2oJjifaDVhmMwTTEf4RrWbvdqMocer22zAnF1jIUitmh4Q%2B%2BLdwbYa%2FnCv3L4NPvL8sBBatUPsK%2FTWQBusapxfud0OvNWqGX0dJTGHY%2Fnw0DgUR0Ks%2BBw%2FEe%2B8wfPVxf3368v4mpwVqSzLIk3%2BtERZjRna%2B8i7DaHrF%2BfnwzAkpzDPd6r79NO53Q0coFnK2Qpdg19mMsGil6L8LFa0qpKU55LlsxsVbNgbuFWPS3STyqrisxvXbo4oFQgj%2FkbXtkvBkzTn7K0uopQXWSKqosxm35wPy5xezjB1HfjwdIdNc%2BXdvru%2BXPIj%2Bg2U19souzZLNrvzqu2VDta1EyZmqz1WtdVPy9XFZSwijOJTERG78xZr5m8hbB3OCN6VsVFrTLmJygZqtW9CvMam0o3qe6sN9A%2FBdeTldVZSVmV5VmScTbNSYpqmSekO06TIt9pSsqzi77UnavraatD%2Bx168tz%2FY12GvlSm51iXlpi6oLGqcc1MyKti6znkqCybX5ETJOcMQWDpR8vL0ovq0PyqldZXTQtWCcg6aVszklAncLJrH7ZCSv16Jrv4RZftKeUrwR7aO7cJkOC07JlkRk%2F4h46PPD3l7efkN%22%7D; _gali=ListViewPagination_Bottom',
        'origin': 'https://www.realtor.ca',
        'referer': 'https://www.realtor.ca/',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    }

    data = {
        'ZoomLevel': '4',
        'LatitudeMax': '64.86294',
        'LongitudeMax': '-23.33496',
        'LatitudeMin': '41.73033',
        'LongitudeMin': '-175.29785',
        'Sort': '6-D',
        'PropertyTypeGroupID': '1',
        'PropertySearchTypeId': '0',
        'TransactionTypeId': '2',
        'Currency': 'CAD',
        'RecordsPerPage': '12',
        'ApplicationId': '1',
        'CultureId': '1',
        'Version': '7.0',
        'CurrentPage': str(i),
    }

    response = requests.post('https://api2.realtor.ca/Listing.svc/PropertySearch_Post', cookies=cookies,
                             headers=headers, data=data)
    result = response.json()
    items = result['Results']
    for item in items:
        try:
            # Address
            address.append(item['Property']['Address']['AddressText'])
        except:
            address.append('')

        try:
            # bedrooms
            bedrooms.append(item['Building']['Bedrooms'])
        except:
            bedrooms.append('')
        try:
            # bathrooms
            bathrooms.append(item['Building']['BathroomTotal'])
        except:
            bathrooms.append('')
        try:
            # agent_name
            agent_name.append(item['Individual'][0]['Name'])
        except:
            agent_name.append('')

        try:
            # aria_code
            aria_code.append(item['Individual'][0]['Phones'][0]['AreaCode'])
        except:
            aria_code.append('')
        try:
            # telephones
            telephones.append(item['Individual'][0]['Phones'][0]['PhoneNumber'])
        except:
            telephones.append('')
        try:
            # prices
            price = item['Property']['Price']
            price_num = float(price.replace("$", "").replace(",", ""))
            prices.append(price_num)
        except:
            prices.append(0)
        try:
            # highrespath
            highrespath.append(item['Property']['Photo'][0]['HighResPath'])
        except:
            highrespath.append('')
        try:
            # medrespath
            medrespath.append(item['Property']['Photo'][0]['MedResPath'])
        except:
            medrespath.append('')
        try:
            # lowrespath
            lowrespath.append(item['Property']['Photo'][0]['LowResPath'])
        except:
            lowrespath.append('')
        try:
            # descriptions
            descriptions.append(item['PublicRemarks'])
        except:
            descriptions.append('')


df_real = pd.DataFrame(
    {
        'address': address,
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'agent_name': agent_name,
        'aria_code': aria_code,
        'telephones': telephones,
        'prices': prices,
        'highrespath': highrespath,
        'medrespath': medrespath,
        'lowrespath': lowrespath,
        'descriptions': descriptions
    }
)

import_data = sqlalchemy.create_engine('postgresql://postgres:02112001@localhost:5432/real_estate')
df_real.to_sql('real_estate',import_data, if_exists='append',index=False)


