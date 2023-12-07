from product.models import VideoModel,VideoReviews
from rest_framework import serializers   
from django.utils.translation import gettext_lazy as _

class VideoWriteSerializer(serializers.ModelSerializer):
    description = serializers.CharField(style={'base_template':'textarea.html','rows':15})    
    #image = serializers.ImageField(max_length=None,allow_empty_file =True, use_url=True,allow_null=False,required=False)      
    
    class Meta:
        model = VideoModel            
        fields = ['category','title','video_file','description',"price","quantity"]   
        
class VideoReadSerializer(serializers.ModelSerializer):        
    
    #url = serializers.SerializerMethodField()         
    
    class Meta:
        model =VideoModel
        fields = ["id","slug","category","get_absolute_url","quantity","video_file","title","description","price","created_at","updated_at"]
        
        
    
    # def get_url(self,obj):
    #    request = self.context.get('request')
    #    abs_url = obj.get_absolute_url()
    #    return request.build_absolute_uri(abs_url)
        

        
    
class VideoReviewsSerializer(serializers.ModelSerializer):  
       
       
    class Meta:
        model = VideoReviews
        fields = ["id","product_id","user_id","review","rating","created_at"]
        depth = 1
 



        
    
        
        
