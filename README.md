# Language-Detector

The language detector uses nltk and sklearn and has been trained on a Wikipedia articles of Nature, Wikipedia, Machine Learning, USA, Shamanism, and 10 random articles.

The data is sourced from [data_harvester.ipynb](https://github.com/babyygemperor/Language-Detector/blob/main/data_harvester.ipynb)

The training code can be seen in [detect.ipynb](https://github.com/babyygemperor/Language-Detector/blob/main/detect.ipynb)

## Usage

Either you can run the [detect.ipynb](https://github.com/babyygemperor/Language-Detector/blob/main/detect.ipynb) notebook or use the Flask App.

```shell
python3 -m flask run
```

You can then get predictions by CURL or the Web UI at [127.0.0.1:5000](http://127.0.0.1:5000/).

```shell
curl -X POST -H 'Content-Type: application/json' -d '{"predict" : "Danskene har en potet i halsen"}' localhost:5000/predict
```