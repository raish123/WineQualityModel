from src.Wine.Exception import CustomException
import os,sys


try:
    a = 1/0
except Exception as e:
    raise CustomException(e,sys)