# Abstract class SocialMedia with abstract method post_content().
# Subclasses:
# Instagram :  " Posting photo with filter "
# Twitter   : " Tweeting with hashtag."
# LinkedIn : " Sharing a professional update."
# from abc import ABC, abstractmethod

# class SocialMedia(ABC):
#     @abstractmethod 


from abc import ABC, abstractmethod

class SocialMedia(ABC):
    @abstractmethod
    def post_content(self):
        pass

class Instagram(SocialMedia):
    def post_content(self):
        print("Posting photo with filter")

class Twitter(SocialMedia):
    def post_content(self):
        print("Tweeting with hashtag")

class LinkedIn(SocialMedia):
    def post_content(self):
        print("Sharing a professional update")


social_media_platforms = [Instagram(), Twitter(), LinkedIn()]

for platform in social_media_platforms:
    platform.post_content()

     