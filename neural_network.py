from neuron import NeuralNetwork


def main():
    nw = NeuralNetwork()
    input_data = [1.0, 2.0, 3.0]
    print("Output: " + str(nw.commit(input_data)))


if __name__ == '__main__':
    main()
