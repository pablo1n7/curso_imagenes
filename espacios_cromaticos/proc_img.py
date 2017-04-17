import numpy as np

MATRIX_RGB_to_YIQ = np.array([[0.299,0.587,0.114],
                            [0.595716,-0.274453,-0.321263],
                            [0.211456, -0.522591, 0.311135]])

MATRIX_YIQ_to_RGB = np.array([[1,0.9663,0.6210],
                            [1,-0.2721,-0.6474],
                            [1, -1.1070 , 1.7046]])

def RGB_to_YIQ(img):
    img_normalize= normalize_RGB(img)
    img_normalize = img_normalize.dot(MATRIX_RGB_to_YIQ)
    return img_normalize

def normalize_RGB(img):
    return img / 255

def unnormalized_RGB(img):
    return np.array(np.round(img * 255),dtype=int)

def YIQ_to_RGB(img_YIQ):
    # que el Y no sea mayor a 1
    img_YIQ = img_YIQ.dot(MATRIX_YIQ_to_RGB)
    img_YIQ[:,:,0][img_YIQ[:,:,0]>1] = 1.0
    # img_YIQ[:, :, 1][img_YIQ[ :, :, 1] > 0.5957]  = 0.5957 
    # img_YIQ[:, :, 1][img_YIQ[ :, :, 1] < -0.5957] = -0.5957
    # img_YIQ[:, :, 2][img_YIQ[ :, :, 2] > 0.5226]  = 0.5226
    # img_YIQ[:, :, 2][img_YIQ[ :, :, 2] < -0.5226] = -0.5226
    
    return unnormalized_RGB(img_YIQ)
    
    #return unnormalized_RGB(img_RGB)


    # que el IQ este entre los valores validos

def change_YIQ(img_RGB,alpha,beta):
    img_YIQ = RGB_to_YIQ(img_RGB)
    img_YIQ[:,:,0] = img_YIQ[:,:,0] * alpha
    img_YIQ[:,:,1] = img_YIQ[:,:,1] * beta
    img_YIQ[:,:,2] = img_YIQ[:,:,2] * beta
    return YIQ_to_RGB(img_YIQ)