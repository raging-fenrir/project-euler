import numpy as np

matrix = np.loadtxt("11.data")
pre_product = 0

for i in range(17):
    for j in range(17):
        post_product = matrix[i][j]*matrix[i][j+1]*matrix[i][j+2]*matrix[i][j+3]
        if post_product > pre_product:
            pre_product = post_product
        
        post_product = matrix[i][j]*matrix[i+1][j]*matrix[i+2][j]*matrix[i+3][j]
        if post_product > pre_product:
            pre_product = post_product
        
        post_product = matrix[i][j]*matrix[i+1][j+1]*matrix[i+2][j+2]*matrix[i+3][j+3]
        if post_product > pre_product:
            pre_product = post_product
        
        post_product = matrix[j][i]*matrix[j+1][i+1]*matrix[j+2][i+2]*matrix[j+3][i+3]
        if post_product > pre_product:
            pre_product = post_product
        
        post_product = matrix[i+3][j]*matrix[i+2][j+1]*matrix[i+1][j+2]*matrix[i][j+3]
        if post_product > pre_product:
            pre_product = post_product

print pre_product    
