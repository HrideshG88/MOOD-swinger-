from azure.storage.blob import BlockBlobService 
from azure.storage.blob import ContentSettings 
import picamera 

camera = picamera.PiCamera() 
camera.capture('image2.jpg') 

block_blob_service = BlockBlobService(account_name='camstoragepi', account_key='psGwTUl4jEvnos15W2boLZlDJsc9sp2xwDHY+zOVygKQ76sw6ObixvSnG6eDHX7JpJTTnRQkduQi5HJAahid7A==') 
block_blob_service.create_blob_from_path( 
   'file.jpg', 
   'fil.jpg', 
   'image2.jpg', 
   content_settings=ContentSettings(content_type='image/jpeg')) 
