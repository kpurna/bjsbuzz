from django.http import Http404,HttpResponse, HttpResponseBadRequest
import json
from django.conf import settings
from bjsbuzzApp.db import query
import time
from datetime import datetime, date
import decimal, simplejson
from django.core.serializers.json import DjangoJSONEncoder

class DecimalJSONEncoder(simplejson.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalJSONEncoder, self).default(o)

def datetime_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError("Unknown type")

def user_details(request):
    limit=request.REQUEST.get('limit','25')
    offset=request.REQUEST.get('offset','0') 
    id = request.REQUEST.get('id','')
    name = request.REQUEST.get('username','')
    email_id = request.REQUEST.get('email_id','')
    where = "";     
    if(id !=""):
        sql = "SELECT * from users WHERE id= %s "
        param_for_user_details=[id]    
        result = query(sql,*param_for_user_details)      
        result_count = len(result)
        if result_count == 0:
            return HttpResponseBadRequest(content="Id does not exist in database")          
        response = {'data':result}     
    else:
        where = "1=1"
        param_for_user_list=[] 
        if(name !=""):           
            name = "%"+name+"%"
            where += " and UPPER(u.name) like (%s)"
            param_for_user_list.append(name)

        if(email_id !=""):
            email_id = "%"+email_id+"%"
            where += " and UPPER(u.email_id) like (%s)"
            param_for_user_list.append(email_id)

        sql = "SELECT * from users as u where "+ where +" ORDER BY u.id  DESC"                  
        results = query(sql,*param_for_user_list)     
        final_test_map = []  
        metadata_totalcount=0 
        #result is constructed in the expected format
        for result in results:
            metadata_totalcount=metadata_totalcount+1
            # response_map = {}
            # response_map['result'] = json.dumps(result, cls=DjangoJSONEncoder)
            # response_map['result']['last_updated'] = json.dumps(result['last_updated'], cls=DjangoJSONEncoder)
            final_test_map.append(result)
        metadata = {"total_count":metadata_totalcount}
        response = {"metadata":metadata,'data':final_test_map}        
    data = json.dumps(response, cls=DjangoJSONEncoder, encoding="ISO-8859-1")    
    http_response = HttpResponse(data, content_type="application/json")
    return http_response

def userscomments_details(request):
    limit=request.REQUEST.get('limit','25')
    offset=request.REQUEST.get('offset','0') 
    id = request.REQUEST.get('comment_id','')
    where = "1=1"
    param_for_user_list=[]
    sql = "select * from users_comments where is_answered = 0 order by comment_id desc"                  
    results = query(sql,*param_for_user_list)
    result_count = len(results)
    if result_count == 0:
        return HttpResponseBadRequest(content="No questions is there to answer")               
    final_test_map = []  
    metadata_totalcount=0 
    #result is constructed in the expected format
    for result in results:
        metadata_totalcount=metadata_totalcount+1
        final_test_map.append(result)
    metadata = {"total_count":metadata_totalcount}
    response = {"metadata":metadata,'data':final_test_map}        
    data = json.dumps(response, cls=DjangoJSONEncoder, encoding="ISO-8859-1")    
    http_response = HttpResponse(data, content_type="application/json")
    return http_response
