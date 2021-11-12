from src.transformation import Transformation
import argparse




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Input data.')
    parser.add_argument('--input', 
                    type=str,
                    help='pass the input json file path' )

    parser.add_argument('--output', 
                    type=str,
                    help= "type in the output data file path")

    args = parser.parse_args()

    print('inputfile:', args.input)
    print('outputfile', args.output)

    application = Transformation(args.input)

    application.save(args.output)
    