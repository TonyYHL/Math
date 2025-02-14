from math import comb

def layerOfDiff(p:int):
    layer1 = [r**p for r in range(1,2+p+1)]
    layers :list[list] = []
    layers.append(layer1)
    for i in range(1,p+1):
        layers.append([layers[i-1][r+1] - layers[i-1][r] for r in range(len(layers[i-1])-1)])
    for i, layer in enumerate(layers):
        print(f"Layer {i+1}: ",layer)

def L(n,k,p):
    """Compute the nth element in kth layer of difference from power sequence of exponent p."""
    return sum([ (-1)**(r+1) * (n+k-r)**p * comb((k-1),(r-1)) for r in range(1,k+1)])

if __name__ == "__main__":
    layerOfDiff(3)
    print(L(3,2,3))
