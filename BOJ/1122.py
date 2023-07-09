def estimate_auroc(X, Y):
    auroc = 0.0  # Initialize the AUROC value
    
    for i in range(len(X) - 1):
        # Calculate the trapezoidal area between two consecutive points
        area = (X[i+1] - X[i]) * (Y[i] + Y[i+1]) / 2.0
        
        # Add the area to the AUROC value
        auroc += area
    
    return auroc


# Example usage
x = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
y = [0.0, 0.2, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.9, 0.95, 1.0]
result = estimate_auroc(x, y)
print(result)