import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config( 
  cloud_name = "theakira", 
  api_key = "146484264375911", 
  api_secret = "AT_-DcdkT9Iv3wq45RNShY30aq0" 
)

cloudinary.uploader.upload("1.jpg")