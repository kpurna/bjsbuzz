from tastypie.resources import ModelResource
from bjsbuzzApp.models.users import Users, UsersComments
from tastypie.authorization import Authorization

class UsersResource(ModelResource):
	class Meta:
		collection_name="data"
		queryset = Users.objects.all()
 		resource_name = 'users'
		authorization = Authorization()
# 		excludes = ['last_login','id']
#   		fields=["email_id","name"]
# 		list_allowed_methods = ["post","get","put","patch"]        
# 		detail_allowed_methods = ["get","put","patch","delete"]

class UsersCommentsResource(ModelResource):
	class Meta:
		collection_name="data"
		queryset = UsersComments.objects.all()
 		resource_name = 'users-comments'
		authorization = Authorization()