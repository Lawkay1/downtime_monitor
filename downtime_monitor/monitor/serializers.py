from rest_framework import serializers
from .models import Website, Emails

class EmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Emails
        fields = ['address']


class WebsiteSerializer(serializers.ModelSerializer):
   # emails = EmailSerializer(many=True, required=False)
    status = serializers.HiddenField(default='UP')
    class Meta:
        model = Website
        fields = ['weburl','status']

'''
    def create(self, validated_data):
        emails_data = validated_data.pop('emails')
        
        if len(emails_data) > 5:
            raise serializers.ValidationError("Maximum number of mails allowed is 5")
        
        website = Website.objects.create(**validated_data)
        
        for mail_data in emails_data:
            Emails.objects.create(website_id=website, **emails_data)
        return website
'''