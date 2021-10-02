# CustomVisualization
Make code snippets of figures more reusable.


## How to run tests
* 1. go into your project directory
```bash
cd 'your-project-directory'
```

* 2. run following command
```bash
## run all tests
python3 -m unittest discover -v tests

## run one test file
python3 -m unittest -v tests/testbar.py

## run one test case
python3 -m unittest -v tests.testbar.TestBar.test_demo

```