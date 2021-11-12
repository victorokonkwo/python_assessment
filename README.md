## Getting Started

This is a step by step guide on setting up your the project application.

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

### Installation
After creating and activating the environment.

1. Clone the repo
    ```sh
    git clone 
    ```

2. Navigate to the file directory

    ```sh
    cd Desktop/python_assessment

    ```

3. Run the tests
    <li>
        Navigate to the test directory.
    </li>

    ```sh
    cd test/
    ```
    <li>
        Run test with pytest
    </li>

    ```sh
    pytest test/
    ```

4. Run the main application

    ```sh 
    python app.py --input ./data/data_1.json --output ./schema/schema_1.json
    ```






