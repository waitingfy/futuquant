#-*-coding:utf-8-*-

from futuquant import *
import pandas

class GetReferenceList(object):

    def test1(self):
        quote_ctx = OpenQuoteContext(host='127.0.0.1',port=11111)
        ret_code, ret_data = quote_ctx.get_referencestock_list(code = 'HK.00700', reference_type = SecurityReferenceType.WARRANT)
        pandas.set_option('max_columns', 100)
        pandas.set_option('display.width', 1000)
        print(ret_code)
        print(ret_data)
        # print(ret_data.columns)
        # i = 0
        # for data in ret_data.values:
        #     print(i,data)
        #     i+=1

if __name__ == '__main__':

    grl = GetReferenceList()
    grl.test1()