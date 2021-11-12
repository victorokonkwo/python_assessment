## Getting Started

This is a step by step guide on setting up the project application.

### Prerequisites

You'll need to create a new environment using anaconda prompt. You can download [Anaconda](https://www.anaconda.com/)

```sh
conda create -n pytest python=3.8
```

```sh
conda activate pytest
```

The next thing you'll need to do is to install pytest to run the test.

```sh
pip install pytest
```

### Instructions
After creating and activating the environment.

1. Clone the repo
    ```sh
    git clone https://github.com/victorokonkwo/python_assessment.git
    ```

2. Navigate to the file directory

    ```sh
    cd Desktop/python_assessment

    ```

3. Run the tests

    ```sh
    pytest test/
    ```

4. Run the main application
    The input arg points to where the data is located and the output arg points to where the json data will be stored

    ```sh 
    python app.py --input ./data/data_1.json --output ./schema/schema_1.json
    ```






